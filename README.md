# Ancient India — A Scientific Heritage

A 34-page HTML presentation redesigned from `main.pptx`, following `INSPIRATION_STYLE_GUIDE.md`.

## Open the presentation

Open `index.html` in Chrome, Safari or another current browser. Keep the `assets` folder beside it. An internet connection loads the CDN libraries and font.

For a local preview, run this command from the presentation folder:

```sh
python3 serve.py
```

Then visit [http://127.0.0.1:4173](http://127.0.0.1:4173). Stop the server with **Ctrl+C**. To use another port, run `python3 serve.py --port 4174`.

## Host on GitHub Pages

The presentation is ready to publish as a static GitHub Pages site. Its asset paths are relative, so it works under a repository URL such as `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`.

1. Create a GitHub repository and upload `index.html`, the complete `assets/` folder, and `.nojekyll` into the repository root. You can also include this README, `.gitignore` and the provenance/style documents.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select the branch containing the files (usually `main`), choose **/ (root)**, and click **Save**.
4. GitHub will show the published website URL on that page after deployment.

These steps follow [GitHub’s publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site). The empty `.nojekyll` file keeps this as a plain static HTML site, following [GitHub’s site-creation guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

There is no server or build step to deploy. `serve.py` is only for local preview. `.gitignore` excludes browser sessions, working files, source PowerPoint and local ZIPs when you use Git from this folder. The portable ZIP also includes the GitHub Pages setup files.

## Present

| Control | Action |
| --- | --- |
| Arrow keys or Space | Move through the slides |
| Home / End | First / last slide |
| O | Slide index |
| N | Notes, original text and supporting sources |
| F | Fullscreen |
| P | Print all slides or save a PDF |
| ? | Keyboard shortcuts |
| Esc | Close a panel |
| Swipe left / right | Move through slides on a touchscreen |

The index and five subject links support direct navigation. On phones, slides become readable vertical pages. Decimal place value, eclipse alignment, city drainage and zinc distillation include interactive examples.

When saving a PDF, choose **Save as PDF**, enable **Background graphics**, and disable browser headers and footers. The presentation supplies its own landscape page size. Printing includes all 34 pages.

## What changed

- All 28 source slides are represented, with their complete original text available in Notes.
- A separate institutional opening retains both original logos and all course details.
- Five minimal explanation pages introduce mathematics, astronomy, architecture, medicine and chemistry after their chapter openers.
- Large editorial typography, looser letter spacing, pale gray backgrounds, fine rules and monochrome imagery follow the supplied inspiration.
- Six original images were generated through the logged-in ChatGPT browser session. See `ASSET_PROVENANCE.md`.
- Visible historical wording was edited for clarity and qualified where the original made uncertain claims. Notes preserve the original wording and explain those changes with linked sources.

The original `main.pptx` is unchanged.

## Files and dependencies

`index.html` contains the presentation markup, styles, metadata and interaction code. `assets/` contains all local imagery. There is no npm installation or build step needed to view it.

Dependencies are delivered only through CDNs: [Tailwind CSS browser 4.3.3](https://tailwindcss.com/docs/installation/play-cdn), [GSAP 3.15.0](https://gsap.com/docs/v3/Installation/) and Google Fonts’ Inter Tight. Versions are pinned for consistent rendering. Essential layout and slide navigation use embedded CSS and native browser APIs; GSAP adds animation. Reduced-motion preferences are respected.

`serve.py` serves only the presentation and its assets on the local machine. Browser storage is kept separately in `.agent-browser-profile/` inside the original workspace and is excluded from the portable ZIP.

For editing in the original workspace, the source is in `work/build_presentation.py`, `work/template.html`, `work/presentation.css` and `work/presentation.js`. Regenerate the HTML with:

```sh
python3 work/build_presentation.py
```

## Verification

The final deck was checked for navigation, chapter links, all interactive examples, index and notes behavior, image loading, desktop and phone layout, and printing as 34 landscape pages. Verification files and preview images are retained in `work/` in the original workspace.
