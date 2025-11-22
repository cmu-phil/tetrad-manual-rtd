# Note Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/note-box.png
:name: tetrad-note-box-screenshot
:alt: Note Box in the Tetrad interface.

Note Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Note** box is where you keep **free-form notes and annotations** inside a Tetrad project.
Notes are lightweight text objects that live alongside your data, graphs, models, and searches, and
are saved with the project file.

You use this box to:

- Record ideas, hypotheses, and decisions made during analysis.
- Document which graphs or models correspond to which experimental conditions or assumptions.
- Keep a simple log of what you tried and what you plan to try next.

## Typical workflow

1. **Create a new note**
   - In the Note box, click **New** to create a note.
   - Give the note a **descriptive title** (e.g., “Fire data: FCI runs with selection bias off”).

2. **Write and edit content**
   - Select the note in the list to open it in the main panel.
   - Type or paste text describing:
     - What you did (e.g., which algorithms and parameters).
     - Why you made certain choices.
     - Observations or interpretations of results.
   - Edit the note as your analysis evolves.

3. **Refer to objects in the project**
   - Use variable names, graph names, dataset names, or model names in your notes so that it is easy to
     cross-reference with other boxes.
   - Optionally maintain simple sections such as “To do”, “Open questions”, and “Conclusions”.

4. **Save and reuse**
   - Notes are stored inside the Tetrad project file.
   - When you reopen a project, your notes are there to remind you where you left off and why certain
     choices were made.

## Key controls

- **Toolbar**
  - **New** – create a new note.
  - **Rename / Delete** – manage existing notes.
  - (Depending on version) **Export** – write the contents of a note to a text or Markdown file.

- **Note list**
  - Shows all notes in the project.
  - Selecting a note loads its text in the editor in the main panel.

- **Main panel**
  - A text editor where you can:
    - Type or paste arbitrary text.
    - Make quick edits while switching between other boxes.

## Common patterns & tips

- Use notes as a **lab notebook**:
  - Record parameter settings, dataset versions, and algorithm choices for each major run.
  - Summarize results and interpretations, especially before closing a project.
- Keep multiple notes:
  - One note per dataset or project subtask.
  - A “Summary” note that collects high-level conclusions.
- When collaborating, share projects with well-maintained notes so others can follow your reasoning
  without hunting through logs and configuration panels.

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Note**:
  - All other boxes, indirectly, since notes are used to document work done with data, graphs, models,
    searches, and simulations.
