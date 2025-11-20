# Change Log

This page summarizes **documentation-only changes** to the  
**Tetrad ReadTheDocs Manual**.  
Software-level release notes remain on GitHub:

👉 **Tetrad Releases (official version history)**  
https://github.com/cmu-phil/tetrad/releases

---

## 📘 Manual Revision History (RTD Manual)

## 2025-02 to 2025-03 — Major Manual Rebuild

A complete modernization and restructuring of the Tetrad manual:

### 🔧 1. Migration from “Classic Manual” to RTD (MyST Markdown)
- Converted the entire older single-HTML “classic manual” into:
    - Modular **MyST Markdown** pages
    - Clean folder structure
    - ReST-compatible images and cross-references
- Removed outdated or redundant content, with pointers to the classic manual when historically relevant.

### 🧭 2. New Sidebar & Navigation Layout
- Created a reorganized, multi-section navigation tree:
    - *Search Algorithms*
    - *Scores & Tests*
    - *Graph Types*
    - *Data Formats*
    - *Interface Documentation*
- Added **Graphs and DataSets** top-level page to connect related topics.

### 🧮 3. Full Rewrite of Algorithm Pages
Completely rewritten, modern, consistent algorithm pages for:

- **BOSS**, **BOSS-FCI**
- **GRaSP**, **GFCI**, **RFCI**
- **FCI**, **CCD**, **CD-NOD**
- **CStaR**, **DM**, **DirectLiNGAM**, **LINGAM**
- **CAM**, **FGES**, **PC**, **PC-Max**
- **Stability Selection**, **FASK**, **LiNGAM variants**
- Others as applicable

Each algorithm page now includes:

- Clear “When to Use / When Not to Use”
- Internal structure & theory summaries
- Correct rule-set descriptions (e.g., **Zhang 2008** orientations for PAGs)
- Fully accurate parameter tables based on code introspection
- Updated references in consistent format

### 📄 4. Standardized Parameter Tables
Every algorithm page now uses a unified table format with **camelCase** parameter names drawn directly from:

```
getParameters() { … }
```

in Java classes.  
Descriptions rewritten for consistency and technical accuracy.

### 🖼️ 5. Image Extraction and Embedding
- Extracted all images from the classic HTML manual.
- Added conversion utilities to embed them into the RTD build.
- Normalized filenames and redirected all references.
- Created `_static/images/` asset directory for long-term stability.

### 🔗 6. Cross-References Throughout the Manual
- Added cross-links between related algorithms (e.g., BOSS → BOSS-FCI → FCIT).
- Connected graph formats, data formats, interface pages, and parameter listings.
- Ensured that all internal links resolve correctly in Sphinx.

### 📚 7. Expanded Papers & Books Page
- Added full bibliography covering:
    - BOSS & GST
    - GRaSP
    - FCI, RFCI, GFCI, and Zhang’s orientation rules
    - DM (latent-spring interpretation)
    - DirectLiNGAM
    - CD-NOD
    - Stability selection
    - High-dimensional consistency
    - Classic works (CPS, Meek 1995, etc.)
- Organized alphabetically by first author.

### 🧑‍🤝‍🧑 8. Updated About & Contributors Pages
- Revised **About** to describe the modern Tetrad platform.
- Updated **Contributors** to reflect both the historical team and contemporary maintainers.
- Added explicit mention of the Py-Tetrad / RPy-Tetrad ecosystem and cross-language integration.

### 🧪 9. Added Missing GUI Documentation
Several parts of the GUI (added over the last few years) lacked documentation.  
Pages now include:

- Updated screenshots
- Clear descriptions of new features
- Corrected or replaced outdated claims

### 🧹 10. Cleanup & Modernization
- Removed obsolete algorithm descriptions superseded by modern methods.
- Removed multi-page outdated guidance now superseded by RTD pages.
- Removed deprecated stats guidance, legacy implementation details, and unmaintained scripts.
- Added prominent, emphasized links to the RTD manual in places where the classic manual formerly held technical content.

---

## 2025-03 — Spot Patches and Fixes

- Corrected BOSS “When to Use” section (dense-graph handling).
- Corrected BOSS-FCI orientation description (now explicitly **Zhang-style**, not Meek).
- Rewrote CD-NOD and CCD parameter tables using actual `Params.*` definitions.
- Fixed math markup on the FCI page so that Sphinx can render it correctly (no LaTeX blocks).
- Fixed several pages with unbroken text blocks by splitting into smaller sections.
- Restored missing images for several “box” pages.
- Created boxed-out content pages (Option D) for long conceptual sections such as estimator boxes and parametric model summaries.
- Ensured all algorithm pages pass link-checking in Sphinx.

---

## Earlier Documentation Notes
Any documentation changes prior to 2025 were partially reflected in scattered internal files and are not reproduced here. The RTD manual supersedes all earlier documentation.

---

If you notice pages that still reflect outdated implementations or missing GUI features, please open an issue or send a request — the manual is under active revision.