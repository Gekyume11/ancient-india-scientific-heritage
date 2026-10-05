# Inspiration style guide

> The governing idea: huge, assured typography; quiet, closely edited information; photographs that invite contemplation; and enough empty space for each of those elements to have a distinct voice.

This guide comes from individually inspecting all 11 images in `inspiration/`, each a 1920 × 1080 landscape composition. It captures their shared visual language and their meaningful variations so that future slides can reproduce the design logic.

The approach is close observation in the spirit of Patrick Jane: notice the small clue, compare it against the other references, and distinguish what is visible from what is inferred. Color samples and image dimensions are measured from the JPEGs. Font identities, editable text settings, and the original designer's intentions cannot be established from these raster images; recommendations below are reconstruction choices.

## 1. What the references reveal

These slides feel like an editorial publication laid out across a presentation canvas. A giant headline supplies the emotional emphasis. Smaller uppercase blocks supply the explanation. Thin rules organize some of those blocks. Photographs provide texture, symbolism, and a second source of visual weight.

The apparent simplicity depends on several precise decisions:

- **Scale does most of the expressive work.** A title may be several times the size of a supporting statement and roughly seven to ten times the size of the small body copy.
- **The background is consistently light gray.** The photographs contain true black and white, which makes their tonal range stand apart from the softer canvas.
- **There are two different dark text colors.** Large titles lean toward warm brown-black. Supporting information leans toward a cooler, muted purple-charcoal.
- **Alignment is disciplined even when placement is unexpected.** Titles can sit at the bottom, pictures can start at the top, and supporting copy can occupy distant corners. Local edges still line up.
- **Blank areas are large and continuous.** They separate visual events and make the small clusters of information feel intentional.
- **Brand placement changes.** The repeated two-line wordmark provides continuity, but its location follows the composition.
- **Images are rectangular and materially varied.** Marble, stone, paper, curtains, skin, clouds, smoke, and motion blur give a restrained palette something to feel.

My interpretation of the resulting mood: intellectual, assured, contemplative, slightly austere, and contemporary. The large type makes the statement feel confident; the distant details reward closer attention.

## 2. Reference-by-reference observations

| Reference | Composition and evidence | Rule to carry forward |
| --- | --- | --- |
| [1.jpg](inspiration/1.jpg) | A huge lowercase `philosophy` occupies the middle-left. A nearly full-height Buddha photograph occupies the right. Two compact notes sit at the top; another sits near the bottom. Pale vertical rules establish narrow information columns. A small light circle appears inside the image near its upper-right corner. | Use one word as a visual anchor. Let small annotations surround it at a distance. Balance a large text mass against a large image. Treat the circle as an optional detail specific to this composition. |
| [2.jpg](inspiration/2.jpg) | The two-line title fills the upper-left. A bold statement occupies the upper-right. A small reader photograph and a larger question-mark photograph form a stepped arrangement down the right side. Three information blocks sit low on the left, separated by rules. | Make a collage through offsets and shared edges. Use a large open middle area to keep multiple clusters distinct. |
| [3.jpg](inspiration/3.jpg) | An architectural photograph touches the top and left canvas edges. The left panel continues into a bold paragraph below. A thin vertical line separates it from the wider right panel. The right title spans two large lines; a small underlined label and four columns sit underneath. | A dense historical or explanatory slide can still have a dominant headline. Use a strong panel division and a consistent lower information band. The photograph reaching the edge is a deliberate exception to the usual inset. |
| [4.jpg](inspiration/4.jpg) | Several small explanation blocks occupy the upper region around a tall, blurred figure photograph and a shorter photograph on the far right. The title sits at the bottom-left; a bold definition sits at the bottom-right. A broad quiet band separates the upper and lower content. | A title can conclude the visual composition. Keep upper modules aligned and preserve the horizontal pause above the bottom headline. |
| [5.jpg](inspiration/5.jpg) | An enormous title stretches across the top. A bold definition is isolated at the lower-left. A large reader image fills the lower-middle, while a narrower right column places explanatory text over a close-up book photograph. The image bottoms align. | Pair a scene with a detail image. Use the definition as a distant counterweight. A shared lower edge can unify unequal image sizes. |
| [6.jpg](inspiration/6.jpg) | A bold definition occupies the upper-left and the giant title sits at the lower-left. Two narrow columns occupy the right, with very tall pale rules, headings around mid-height, and photographs below. | Long rules can establish the column structure before the text begins. Balance a very large title against smaller text-and-image modules. |
| [7.jpg](inspiration/7.jpg) | The same ethics title moves to the upper-right. A bookshelf photograph anchors the lower-left, with a bold explanatory block beside it. Two ruled information columns occupy the lower-right. The center remains mostly empty. | A shared topic can have a different composition without changing its identity. Preserve the type hierarchy, colors, photo treatment, and local alignments while moving the anchor. |
| [8.jpg](inspiration/8.jpg) | A large, nearly full-height sculptural face photograph occupies the left. A three-line title occupies the upper-middle. A bold paragraph sits in a separate right column. Shorter and longer body blocks occupy the lower-middle and lower-right, divided by thin rules. | Let an evocative image carry substantial visual weight. A three-line headline can serve as a vertical mass between the image and the dense information. |
| [9.jpg](inspiration/9.jpg) | A bold introduction sits at the upper-left, a two-line title at the lower-left, and two similarly sized photographs sit at the upper-right with headings and copy below. The brand moves to the lower-right. | Use equivalent image modules when the content calls for comparison. The continuity comes from the design system, so brand placement can adapt. |
| [10.jpg](inspiration/10.jpg) | A large horizontal statue photograph occupies the lower-left. The headline occupies the lower-right. Two small text blocks sit at the top-right, separated by a vertical rule; the wordmark sits at the top-left. Most of the upper-left and center stay open. | A sparse slide can create a strong diagonal movement: top information, lower image, lower title. Resist filling the quiet center. |
| [11.jpg](inspiration/11.jpg) | A huge two-line closing statement occupies the upper-left. A bold paragraph sits at the upper-right over a dark bust photograph. Contact information sits at the lower-left, while a long body paragraph sits between two vertical rules near the lower-middle. | Close with a clear verbal statement and a strong image. Practical information can remain small and secondary. Replace sample branding and contact details with real content. |

### The especially revealing comparison: references 6 and 7

Both references use the same large title, yet the title moves from the lower-left to the upper-right. Image subjects, column arrangements, and wordmark positions also change. They still unmistakably belong together.

That comparison shows which properties matter most: type character, dramatic scale contrast, restrained colors, rectangular monochrome imagery, thin rules, and the way empty space separates information clusters. Exact headline position is a flexible property.

## 3. Color system

| Role | Value to use | Evidence and application |
| --- | --- | --- |
| Canvas | `#ECECEC` | Measured flat background color, dominant in every reference. Keep the background uniform. |
| Hero headline | `#251A16` | A repeatedly occurring interior headline pixel color. JPEG variation produces neighboring values, but this is a strong reconstruction anchor. |
| Supporting text | Approximately `#403645` | Representative purple-charcoal reconstruction. Small text contains compression and antialiasing variation; samples vary by region. Use a consistent token when rebuilding. |
| Dividers | Approximately `#CDCDCD` | Sampled rules include values around `#CFCFCF` and `#D0D0D0`. Their defining trait is low contrast against the canvas. |
| Photography | Grayscale | Photographic blacks and whites can be substantially stronger than the background and supporting text. Preserve useful midtones. |
| Optional image marker | Light gray, approximately `#D8D8D8` | The small circle in reference 1. It is an isolated accent, not a recurring navigation or numbering system. |

The warm headline and cool supporting copy are a subtle clue. Flattening both into identical pure black would lose some of the references' character. The text palette is almost monochrome, but contains a small temperature difference.

The exact background color accounts for approximately 48–80% of the pixels in individual references. That measurement includes background between letters and other small gaps, so it is not a precise measurement of compositional empty space. It does confirm how extensively the light canvas participates in the overall appearance.

## 4. Typography: the primary design material

### Character

Use a heavy, compact grotesque sans serif for headlines: large counters, broad strokes, straightforward letterforms, and little ornamental personality. The references suggest a Helvetica/Arial-like family, but the exact face is unverified. Select a close available face by comparing the lowercase `a`, `g`, `e`, the capital `R`, and the width of complete words against the references.

Use a related neutral sans serif for supporting text. Headings and statements are bold; paragraph text is regular or medium. A single family with suitable weights is a reasonable reconstruction starting point. The references do not require a serif for their scholarly mood.

### Hierarchy and reconstruction ranges

These are suggested starting ranges for rebuilding a 1920 × 1080 composition. They are estimates of nominal type settings, not recovered source font sizes.

| Role | Approximate nominal size | Weight and treatment |
| --- | --- | --- |
| Short hero or cover word | 160–210 px | Heavy/bold; very tight spacing; one or two lines |
| Longer sectional headline | 110–170 px | Heavy/bold; manually composed line breaks |
| Bold thesis or definition | 24–34 px | Bold; uppercase; compact line spacing |
| Small module heading | 18–24 px | Bold; uppercase |
| Supporting paragraph | 18–22 px | Regular/medium; uppercase; compact but readable |
| Two-line wordmark or contact text | 18–22 px | Bold; uppercase where appropriate |

For a standard 13⅓ × 7½-inch PowerPoint slide rendered at 1920 × 1080, 1 point occupies approximately 2 pixels. Thus a nominal 160 px title corresponds to approximately 80 pt, and 22 px body copy to approximately 11 pt. This conversion depends on slide size and export resolution.

The small body copy in these examples is suited to close viewing. For a projected presentation, increase it as needed and reduce the words per module so that the same visual hierarchy remains readable.

### Spacing, line breaks, and case

- Headline letters sit unusually close together. Begin with slightly negative tracking, around `-0.04em`, and tune to the chosen face; a range of roughly `-0.03em` to `-0.06em` is a reconstruction estimate.
- Keep headline lines tight, beginning around `0.95–1.05` line height. Inspect actual glyph bounds before tightening further.
- Supporting copy also has tight leading, roughly `1.0–1.1`. It generally lacks the wide tracking often used for luxury-style uppercase text.
- Most large section titles use title case. The cover word uses lowercase. Small headings, paragraphs, statements, and brand text are uppercase.
- Choose headline breaks by meaning and visual width. Examples such as `Old Questions, / New Urgency` create both a verbal relationship and a balanced pair of shapes.
- Supporting text has a ragged right edge. Narrow measures create dense, short-line blocks.
- Some source titles have extremely narrow word gaps or colon spacing. Carry forward their compactness while retaining readable separation; do not reproduce accidental collisions.

One important distinction: the giant text behaves almost like a solid graphic shape. The small uppercase copy behaves like an information texture. Both must remain legible, but they do different compositional jobs.

## 5. Geometry, alignment, and empty space

### Canvas and margins

All references use a 16:9 canvas. A common outer inset is approximately 42 px, or 2.2% of canvas width and 3.9% of canvas height. Many image and text edges use that inset, and many lower elements end near `y = 1038`.

This is a recurring anchor, not an absolute rule. Reference 3 places its upper-left image directly against the top and left edges. Some giant titles also push closer to the top than the usual inset.

On a standard 13⅓ × 7½-inch slide, the 42 px inset corresponds to approximately 0.29 inches at the reference export scale.

### Grid behavior

The evidence supports a flexible editorial grid with strong local alignments. It does not establish a single fixed 12-column grid across the entire set.

Repeated relationships include:

- Wide headline zones alongside narrower information zones.
- Images and neighboring paragraphs sharing a left or right edge.
- Two or more modules sharing a bottom edge.
- Column separators extending well above the text they organize.
- Supporting blocks aligning along an upper band or a lower band while leaving the center quiet.
- A title and image acting as two large masses, with smaller information clustered around them.

Set the main anchors first. Derive the remaining positions from shared edges and consistent gutters. Avoid placing each object independently by eye.

### Measurable layout anchors

The following coordinates are approximate readings from the images. Origin is the upper-left; values refer to the 1920 × 1080 canvas. They describe visible regions rather than editable text-box boundaries.

| Reference | Useful anchor |
| --- | --- |
| 1 | Right photograph begins around `(1102, 42)` and measures approximately `775 × 995 px`. The hero word occupies the left around `y = 455–635`. |
| 3 | Left upper image occupies approximately `0–601 px` horizontally and `0–556 px` vertically. The main panel division stays near `x = 601`. |
| 4 | Central image begins around `(657, 42)` and measures approximately `384 × 489 px`. Far-right image begins around `(1471, 42)` and measures approximately `406 × 303 px`. |
| 5 | Reader image begins around `(895, 399)` and measures approximately `505 × 640 px`. The book detail begins around `(1435, 632)` and shares its lower edge. |
| 8 | Left image begins around `(42, 10)` and measures approximately `681 × 1027 px`. The title begins around `x = 790`; the outer right information division sits near `x = 1448`. |
| 10 | Lower-left image begins around `(42, 530)` and measures approximately `876 × 510 px`. The lower-right title begins around `x = 1010`. |
| 11 | Lower-right image begins around `(1341, 534)` and measures approximately `536 × 505 px`. The lower body column is bracketed by rules near `x = 495` and `x = 1001`. |

### What the empty space does

It separates the loud headline from the quiet explanation, slows the scan between clusters, and lets the imagery feel significant. In references 4, 6, 7, and 10 especially, a large blank region is part of the composition's structure.

Preserve those continuous blank regions during adaptation. If additional content is necessary, create another slide or shorten the copy before using the quiet middle as a storage area.

## 6. Photography and cropping

### Shared treatment

Every photograph is monochrome, rectangular, and placed without a visible frame, rounded corners, or shadow. Most retain photographic texture. Contrast varies: some pictures are softly gray; others are strongly black and white.

The subjects recur in related groups:

| Subject family | Visible examples | Contribution to the design |
| --- | --- | --- |
| Classical objects and structures | Statues, busts, temple columns | A sense of history, material permanence, and reflection |
| Human contemplation | Reading, sitting alone, a blurred figure | A human scale and an inward-looking mood |
| Books and printed pages | Book spines, open pages, a reader | Detail, learning, and tactile texture |
| Suggestive objects and gestures | Stacked stones, a question mark, interacting hands | A conceptual association without a diagram |
| Ambiguous imagery | Motion blur, smoke around a sculptural head, reflection-like imagery | Uncertainty and an invitation to look again |

These associations are interpretations of the visible subjects. They are useful art-direction cues, not proof of what the original designer intended.

### Practical image rules

- Choose one image that strongly supports the idea of the slide. Add a second when it provides a distinct detail, comparison, or association.
- Crop to give the subject a clear relationship to the text mass. Faces, hands, books, and architectural edges matter more than preserving the full source photograph.
- Retain texture in stone, paper, cloth, and skin. Avoid crushing every grayscale image into the same harsh contrast treatment.
- Allow photographic darkness to balance a large headline. Reference 11's dark portrait and reference 8's large image demonstrate two different ways to do this.
- Use rectangles with different proportions when the layout benefits from them. Equal image sizes are a specific option, demonstrated most clearly in reference 9.
- Keep text on the light canvas in the dominant pattern. The images can remain visually self-contained.

For a different presentation subject, translate these image roles into relevant material. The structural treatment transfers; philosophical statues and book imagery only belong where they support the new content.

## 7. Supporting components

### Rules

Use thin, pale gray vertical lines as column boundaries. At the reference resolution they appear approximately 1–2 px thick. They often begin far above the paragraphs, making the grid visible in otherwise empty space. Leave a clear gutter between a rule and the neighboring copy.

The short horizontal line under the section label in reference 3 is another restrained component. Both kinds of line are subordinate to text and imagery.

### Wordmark

The repeated `NORTH / ACADEMY` mark is small, bold, uppercase, left-aligned within its own two-line block. It appears at the upper-left, upper-right, above an image, or lower-right depending on the slide.

Its stable scale and treatment maintain continuity while its position adapts. For a new deck, use the actual project identity with similarly restrained treatment; the reference's brand is not part of the transferable content.

### Text modules

A common module has a bold uppercase label, a small gap, and a regular uppercase paragraph. Other modules contain only a bold statement or a compact paragraph. The references use these simple combinations repeatedly without enclosing them in panels.

They do not rely on bullet symbols. To adapt a list, consider several concise editorial blocks or separate short paragraphs. Use conventional bullets if the content requires them, keeping their visual weight secondary.

### Contact block and optional circle

Reference 11's contact block is a set of small, separated bold lines. Its hierarchy remains well below the closing headline and portrait. Use verified, real contact details in any adaptation.

Reference 1's circle is the only clear decorative shape of this kind in the set. Its isolated use suggests restraint: it should not become a repeated motif on every slide without a reason.

## 8. Reusable composition families

### A. Cover word and portrait

Use reference 1: a wide left text field, a tall image on the right, a large word around the vertical middle, and two or three distant annotations. Keep the wordmark small. Best for introducing a theme with immediate presence.

### B. Upper headline and lower modules

Use references 2, 3, and 5: a title across the upper region, then supporting information in lower clusters. Choose a left architectural panel, a stepped photo arrangement, or a scene-and-detail image pair according to content.

### C. Lower headline and upper explanation

Use references 4, 6, and 9: place the main statement low on the canvas and organize explanations or image modules above or to its right. Preserve a broad quiet area between regions.

### D. Upper-right headline and lower information band

Use reference 7: a large title occupying the upper-right, a lower-left photo, and supporting copy running along the lower band. Useful for changing the deck's rhythm while keeping the same type system.

### E. Large left image and stacked headline

Use reference 8: an image occupying roughly one-third of the canvas, a large stacked title beside it, and a narrower outer column for the main explanatory statement. Body details can occupy the lower region.

### F. Sparse diagonal composition

Use reference 10: small information at the top-right, a horizontal image at the lower-left, and a large title at the lower-right. The quiet upper-left and middle are essential to this family.

### G. Closing statement and portrait

Use reference 11: a huge upper-left statement, a right-side paragraph over a strong portrait, and small practical details along the bottom. Give the ending one memorable verbal and visual anchor.

Across a deck, alternate these families based on content. The sources demonstrate variation within a stable visual language rather than a single repeated layout.

## 9. The subtle clues to preserve

**Typography creates authority; texture gives it warmth.** The heavy sans serif could feel mechanical on its own. Photographic grain, sculptural surfaces, old books, and cloth introduce material detail.

**Large text and dense small text invite two speeds of reading.** The headline communicates immediately. The supporting clusters require attention. In a live presentation, the speaker can carry some of the detail so that small text does not become a reading burden.

**The balance is based on visual mass.** A small dark image can balance a wider light region. A large headline can balance a tall photograph. Matching object dimensions is less important than understanding which areas attract the eye.

**The dividers make otherwise invisible organization perceptible.** Their low contrast keeps them quiet, while their length establishes clear column relationships.

**The brand behaves like a signature.** It stays small and recognizably consistent while moving around the page. Its placement helps the composition rather than dictating the entire layout.

**Different layouts carry the same identity.** The repeated palette, typographic character, image treatment, and scale relationships make movement between layouts feel coherent.

**The photographs suggest questions.** Several pictures are symbolic or ambiguous rather than explanatory. That gives the deck a reflective quality. Use this approach where ambiguity serves the subject; use concrete evidence where clarity is the priority.

## 10. Applying this style to future slides

1. Identify the single statement the audience should remember. Write a headline that can carry it in one to three large lines.
2. Choose the composition family that fits the content. Decide where the headline and image will create the main visual masses.
3. Select and crop relevant monochrome imagery. Check subject placement, tonal weight, and texture.
4. Establish outer insets, shared edges, and column boundaries before placing the small copy.
5. Add only the supporting information needed for this slide. Separate a bold thesis from finer explanations through weight and scale.
6. Tune headline spacing and manual line breaks. Preserve letter clarity at the actual viewing size.
7. Add rules and project identity where they help organize the composition.
8. Check the slide as a thumbnail for hierarchy, then at presentation size for readability. Adjust density while protecting the large quiet areas.

Source wording is inspiration material, not a verified factual reference. Historical names and attributions should be checked separately if used; sample contact details and branding should be replaced.

### Review criteria

- A dominant headline is immediately apparent.
- The background, headline ink, supporting ink, and rule colors remain consistent.
- Photographs are relevant, monochrome, rectangular, and carefully cropped.
- Text and image edges reveal a deliberate grid.
- Empty space remains continuous enough to separate the main clusters.
- Headlines have deliberate line breaks and compact spacing without unintended overlaps.
- Small copy is readable for the intended audience and viewing conditions.
- The layout contributes to the deck's rhythm while maintaining its shared identity.

### Changes that would materially alter the reference style

Bright accent colors, gradients, repeated rounded cards, prominent shadows, decorative icons, centered body paragraphs, uniformly sized text, and crowded use of the middle would all change the visual language substantially. Apply such additions only when the new content requires that change.

## 11. Compact implementation brief

> Build a 16:9 editorial presentation on a uniform `#ECECEC` background. Use enormous, tightly spaced grotesque headlines in warm brown-black `#251A16`, with compact uppercase supporting text in muted purple-charcoal around `#403645`. Organize information through shared edges, narrow columns, and pale 1–2 px rules. Use rectangular monochrome photographs with tactile detail and purposeful crops. Balance strong headline and image masses across asymmetric compositions, preserving broad continuous empty regions. Keep the project identity small and consistent in treatment, adapting its position to each layout. Vary among upper-title, lower-title, image-led, comparison, and sparse diagonal compositions. Adjust supporting type and word count for the actual viewing conditions while preserving the dramatic scale hierarchy.

This brief can guide future design work alongside the individual references above. The essential quality is the relationship between the elements: a forceful statement, a quiet explanation, a meaningful image, and carefully held space between them.
