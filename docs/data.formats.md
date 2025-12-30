# Data Types and Formats

Tetrad accepts several file formats for loading **datasets**, **covariance matrices**,  
and **correlation matrices**. This page documents all currently supported formats.

The goal is to eliminate common parsing errors and clarify exactly what Tetrad expects.

---

## 1. Overview of Supported Formats

Tetrad supports:

- **Tabular data files** (continuous, discrete, or mixed)
- **Covariance matrices** (full square or legacy lower-triangular)
- **Correlation matrices** (full square or legacy lower-triangular)

This page covers these **data formats**.

---

## 2. Dataset Format (Tabular Data)

Tabular datasets must follow this structure:

1. **Header row:** variable names  
2. **One data row per case**  
3. **Values separated by tabs, commas, or spaces**

Example:

```text
X Y Z
1.2 5.0 3
0.9 4.8 3
1.4 5.1 2
```

### Notes

- Missing values are written by default as: `*`, though other options are also supported.
- Mixed data (continuous + discrete) is allowed.
- Variable order in the header determines column order throughout the file.
- It is important not to end a line with a delimiter, as this can cause parsing errors.

---

## 3. Discrete Data

Discrete data follows the same structure but the values must be **integers or strings**  
representing categories.

Example:

```text
A B C
0 1 yes
1 0 no
2 1 yes
```

---

## 4. Continuous Data

Continuous data uses the same tabular format, but all values should be numeric:

```text
HEIGHT WEIGHT AGE
66.1 150.2 33
70.3 182.4 44
```

---

## 5. Covariance and Correlation Matrices

Tetrad now supports **two equivalent file formats** for covariance and correlation matrices:

1. A **full square matrix**, preceded by a sample-size line and a variable-name line (current default)  
2. A **lower-triangular matrix** preceded by a sample-size line and a variable-name line (still fully supported for backward compatibility)

Both formats use the same header:

1. **Sample size** (integer, on its own line)  
2. **Variable names** (space-separated or tab-separated)  
3. **Matrix values** (either full square or lower-triangular)

Any deviation from this structure will cause Tetrad to reject the file.

---

### 5.1 Required Structure

A valid covariance/correlation file must contain:

1. **Sample size** (integer, on its own line)  
2. **Variable names** (space-separated or tab-separated)  
3. **Matrix body**, in one of the two supported shapes:

Here p is the number of variables (the number of names on the header line).

- **Lower-triangular format**
  - Row 1: 1 value
  - Row 2: 2 values
  - …
  - Row p: p values
  
- **Full square format (current default)**  
  - Row 1: p values  
  - Row 2: p values  
  - …  
  - Row *p*: `p` values
  
---

### 5.2 Lower Triangle Covariance Matrix Example

Below is a complete, valid **lower-triangular** covariance file.  
This is a classic example that has been used by Tetrad historically.

```text
164
ABILITY GPQ PREPROD QFJ SEX CITES PUBS
1.0
 .62 1.0
 .25 .09 1.0
 .16 .28 .07 1.0
 -.10 .00 .03 .10 1.0
 .29 .25 .34 .37 .13 1.0
 .18 .15 .19 .41 .43 .55 1.0
```

#### Important Characteristics of the Lower Triangular Format

- **Line 1:** sample size (`164`)  
- **Line 2:** variable names (7 variables)  
- **Lines 3–9:** lower triangle of the covariance matrix  
- Whitespace before numbers is acceptable  
- Diagonal entries must be included (`1.0` above)  
- No commas (`1,0` is invalid)  
- No extra blank lines at the end  
- The number of rows in the lower triangle must equal the number of variables
- It is important not to end a line with a delimiter, as this can cause parsing errors.

This format is still accepted for both covariance and correlation matrices.

---

### 5.3 Full Square Covariance Matrix Example (Current Default)

When a covariance matrix is **exported from Tetrad**, it is now written in full square format.  
The same example as above, written as a full `7 × 7` matrix:

```text
164
ABILITY GPQ PREPROD QFJ SEX CITES PUBS
1.00   0.62  0.25  0.16 -0.10  0.29  0.18
0.62   1.00  0.09  0.28  0.00  0.25  0.15
0.25   0.09  1.00  0.07  0.03  0.34  0.19
0.16   0.28  0.07  1.00  0.10  0.37  0.41
-0.10  0.00  0.03  0.10  1.00  0.13  0.43
0.29   0.25  0.34  0.37  0.13  1.00  0.55
0.18   0.15  0.19  0.41  0.43  0.55  1.00
```

You may use tabs, spaces, or the chosen delimiter; the key requirement is that:

- The matrix is **square**, with exactly p values on each of p lines,  
- The order of variables matches the header line.
- It is important not to end a line with a delimiter, as this can cause parsing errors.

---

### 5.4 Correlation Matrices

Correlation matrices use **the same two formats** as covariance matrices:

- Full square matrix (current export default)  
- Lower triangle (still accepted)

Example (full square):

```text
500
X Y Z
1.0  0.20 -0.10
0.20 1.0   0.35
-0.10 0.35 1.0
```

Lower-triangular example:

```text
500
X Y Z
1.0
 .20 1.0
 -.10 .35 1.0
```

---

### 5.5 Common Parsing Errors for Covariance/Correlation Files

Users often encounter:

- **Missing sample size** (first line must be an integer)
- **Variable names not matching matrix dimensions**  
  - For square format: not exactly p values per row, or not exactly p rows  
  - For lower-triangular format: wrong number of values in a given row
- **Mixing square and triangular conventions** in a single file
- **Trailing blank lines**
- **Use of commas** instead of decimal points
- **Extra text or comments in the matrix region**

Each of these produces a **“Could not parse covariance matrix”** error.

---

## 6. Lower-Triangular Format

The lower-triangular matrix format is kept as a legacy option:

- All existing covariance and correlation files using the old lower-triangular convention  
  will continue to load without modification, provided the user selects the Lower Triangular option.
- New users are encouraged to use the **square format**, which aligns with conventions in R and Python.
- Internally, Tetrad treats both formats as representing the same symmetric matrix.

There is no need to convert existing lower-triangular files unless you prefer the square style.

---

### 6.1 Note on GUI Display

In the Tetrad GUI, covariance and correlation matrices are **currently displayed using only the lower triangle**, even if they were loaded from a full square matrix file. This is purely a **display choice**:

- The matrix is still treated as a full symmetric covariance/correlation matrix internally.
- Only the lower triangle is shown to reduce redundancy and to emphasize that the object is a covariance or correlation matrix.

This behavior is independent of whether the file itself was in square or lower-triangular format.

---

## 7. Exporting Data from Tetrad

Tetrad can export:

- Tabular datasets  
- Covariance matrices  
- Correlation matrices  

Export behavior:

- Covariance and correlation matrices are now exported in **full square format** by default.  
- The **lower-triangular** format is **no longer used for export**, but is still supported for import.

This means:

- You can load either full square or lower-triangular files.  
- When you save from Tetrad, you will get the square form.

---

## 8. Summary

| Format Type                                  | Supported? | Notes                                                       |
|----------------------------------------------|------------|-------------------------------------------------------------|
| Tabular data                                 | ✔          | Standard space/tab/comma-separated file                     |
| Lower Triangle covariance/correlation matrix | ✔ (legacy) | Fully supported for backward compatibility                  | |
| Full covariance/correlation square matrix    | ✔          | Current default import/export format                        |
| Graph formats                                | ✔          | See graph file section                                      |
