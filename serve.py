"""Serve the presentation locally without exposing the browser profile or work files."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse

ROOT = Path(__file__).resolve().parent

class PresentationHandler(SimpleHTTPRequestHandler):
    def prepare_route(self):
        path = unquote(urlsplit(self.path).path)
        if path == '/':
            self.path = '/index.html'
        elif path != '/index.html' and not (
            path.startswith('/assets/') and
            all(part not in ('.', '..') and not part.startswith('.') for part in path.split('/')[1:]) and
            Path(path).suffix.lower() in {'.png', '.webp', '.jpg', '.jpeg', '.svg'}
        ):
            self.send_error(404)
            return False
        return True

    def do_GET(self):
        if self.prepare_route():
            super().do_GET()

    def do_HEAD(self):
        if self.prepare_route():
            super().do_HEAD()

    def list_directory(self, path):
        self.send_error(404)
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Preview the Ancient India presentation')
    parser.add_argument('--port', type=int, default=4173)
    args = parser.parse_args()
    print(f'Presentation: http://127.0.0.1:{args.port}', flush=True)
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(PresentationHandler, directory=str(ROOT)))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
