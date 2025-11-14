# Tetrad Data Formats

Tetrad accepts several file formats for loading **datasets**, **covariance matrices**,  
and **correlation matrices**. This page documents all currently supported formats.

The goal is to eliminate common parsing errors and clarify exactly what Tetrad expects.

---

# 1. Overview of Supported Formats

Tetrad supports:

- **Tabular data files** (continuous, discrete, or mixed)
- **Covariance matrices** (current format: lower-triangular)
- **Correlation matrices** (same lower-triangular format)
- **Graph formats** (listed on a separate page)
- **Simulation input formats** (model specifications, DAG text formats)

This page covers the **dataset** and **matrix** formats.

---

# 2. Dataset Format (Tabular Data)

Tabular datasets must follow this structure:

1. **Header row:** variable names
2. **One data row per case**
3. **Values separated by tabs or spaces**

Example:

```
X Y Z
1.2 5.0 3
0.9 4.8 3
1.4 5.1 2
```

### Notes

- Missing values may be written as: `*`, `?`, or blank.
- Mixed data (continuous + discrete) is allowed.
- Variable order in the header determines column order throughout the system.

---

# 3. Discrete Data

Discrete data follows the same structure but the values must be **integers or strings**  
representing categories.

Example:

```
A B C
0 1 yes
1 0 no
2 1 yes
```

---

# 4. Continuous Data

Continuous data uses the same tabular format, but all values should be numeric:

```
HEIGHT WEIGHT AGE
66.1 150.2 33
70.3 182.4 44
```

---

# 5. Covariance and Correlation Matrices
(Current Tetrad Format)

Tetrad currently supports **only one** matrix format:

> A **lower-triangular matrix**, preceded by a **sample size** line and a **variable-name** line.

This format applies to **both covariance and correlation matrices**.

Any deviation from this structure will cause Tetrad to reject the file.

---

## 5.1 Required Structure

A valid covariance/correlation file must contain:

1. **Sample size** (integer, on its own line)
2. **Variable names** (space-separated or tab-separated)
3. **Lower triangle of the matrix**, written row by row

Matrix layout:

- Row 1: 1 value
- Row 2: 2 values
- ...
- Row *p*: *p* values

The **upper triangle must not appear**.

---

## 5.2 Full Example (Exactly as Tetrad Expects)

Below is a complete, valid covariance file.  
This is the example that users often find confusing, so it is given *in full*.

```
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

### Important Characteristics of This Format

- **Line 1:** sample size (`164`)
- **Line 2:** variable names
- **Lines 3–9:** lower triangle of the covariance matrix
- Whitespace before numbers is acceptable
- Diagonal entries must be included (`1.0` above)
- No commas (`1,0` is invalid)
- No extra blank lines at the end
- Dimensionality must match the number of variables

---

## 5.3 Correlation Matrices

Correlation matrices use **the same format**.

Example:

```
500
X Y Z
1.0
 .20 1.0
 -.10 .35 1.0
```

---

## 5.4 Common Parsing Errors for Covariance/Correlation Files

Users often encounter:

- **Full square matrix instead of lower triangle**
- **Missing sample size** (first line must be an integer)
- **Incorrect number of entries per row**
- **Variable names not matching matrix dimension**
- **Trailing blank lines**
- **Use of commas** instead of decimals
- **Rows not aligned in lower-triangle shape**

Each of these produces a **“Could not parse covariance matrix”** error.

---

# 6. Planned Future Support (Not Yet Available)

Tetrad will soon support **full square covariance/correlation matrices**.  
The planned behavior:

- Users may supply either a *full square matrix* or a *lower triangle*.
- If a full matrix is provided, the **upper triangle will be ignored**  
  (the lower triangle will be used).
- Backward compatibility with the current format will be preserved.

This feature is not yet available, but is under active development.

---

# 7. Exporting Data from Tetrad

Tetrad can export:

- Tabular datasets
- Covariance matrices (in the same lower-triangle format)
- Correlation matrices
- Graphs (separate formats)

Exported matrices will **always** be in the lower-triangular format until  
the square-matrix feature is implemented.

---

# 8. Summary

| Format Type | Supported? | Notes                                   |
|-------------|------------|-----------------------------------------|
| Tabular data | ✔ | Standard space/tab/comma-separated file |
| Covariance matrix (lower triangle) | ✔ | Current required format                 |
| Correlation matrix (lower triangle) | ✔ | Same format as covariance               |
| Full covariance/correlation square matrix | ❌ (not yet) | Will be supported soon                  |
| Graph formats | ✔ | See graph file section                  |
