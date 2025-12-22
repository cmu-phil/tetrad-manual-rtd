# Example: Preparing the Auto MPG Dataset for Causal Analysis

This page walks through how the **Auto MPG** dataset was loaded, examined, and prepared for causal analysis in Tetrad.  
It serves as a concrete example of the **data preparation stage** in the causal analysis workflow.

The goal here is not to “optimize” the dataset, but to make **transparent, defensible preprocessing choices** that align with the assumptions used later in causal discovery.

---

## 1. The Dataset

The Auto MPG dataset contains measurements on automobiles, including fuel efficiency and engine characteristics.  
The variables used in this example are:

- `mpg`
- `cylinders`
- `displacement`
- `horsepower`
- `weight`
- `acceleration`
- `modelyear`
- `origin`

Most variables are continuous.  
The variable **`origin`** is discrete with three categories, representing region of manufacture.

---

## 2. Preprocessing Decisions

Before loading the data into Tetrad, two preprocessing steps were applied.

### 2.1. Removing the Car Name Field

The original dataset includes a **string-valued car name** column.  
This field is purely an identifier and has no causal interpretation.

**Action taken:**
- The car name column was removed before analysis.

**Reasoning:**
- Causal discovery algorithms in Tetrad operate on numerical and categorical variables.
- Identifier fields can introduce spurious structure and should be excluded.

---

### 2.2. Handling Missing Values

The dataset contains a small number of rows with missing values (notably in `horsepower`).

**Action taken:**
- Rows with missing values were removed.

**Reasoning:**
- For this example, simplicity and transparency were prioritized.
- Removing a small number of incomplete rows avoids introducing assumptions implicit in imputation.
- This keeps the example focused on workflow rather than missing-data methodology.

> More advanced workflows may use imputation or model-based handling of missingness; those are discussed elsewhere in the manual.

---

## 3. Loading the Data into Tetrad

The cleaned dataset was loaded into Tetrad as a **mixed dataset**, since it contains both continuous and discrete variables.

### Key Settings Used

- **Data type:** Mixed
- **Maximum number of categories:** 3

This setting reflects the fact that `origin` has exactly three categories, while all other variables are treated as continuous.

---

## 4. Exploring the Data: Plot Matrix

Once loaded, the first step was **visual inspection** using the **Plot Matrix** in the Data Box.

```{figure} ../../_static/images/tetrad-interface/box-by-box/example-data-plotmatrix.png
:name: tetrad-grid-search-box-screenshot
:alt: Plot matrix for the Auto-MPG data.
```

The plot matrix reveals several important features:

- Many variable pairs exhibit **strong linear trends**
- Discrete variables (such as `origin`) produce visible striping patterns
- No obvious multimodal or highly nonlinear relationships dominate the data

This visual evidence supports the use of **linear or approximately linear modeling assumptions** as a reasonable starting point.

> Visual inspection is critical: it informs *which assumptions are plausible* before any algorithm is run.

---

## 5. Implications for Method Choice

Based on the observed structure:

- Relationships appear largely linear
- The data are mixed (continuous + discrete)
- There is no immediate visual evidence demanding nonlinear or nonparametric modeling

This suggests that **linear Gaussian–based scores adapted for mixed data** are appropriate initial choices.

In this workflow, we therefore proceed using the **Degenerate Gaussian likelihood–based score**, which is designed to handle mixed datasets of this form.

This choice is not final or exclusive — it is a **reasonable baseline**, justified by data exploration.

---

## 6. Why This Preparation Matters

Each preprocessing step supports later stages of causal analysis:

- Removing identifiers avoids meaningless structure
- Handling missing values explicitly avoids hidden assumptions
- Declaring data type correctly ensures compatible tests and scores
- Visual exploration grounds assumptions in evidence

By documenting these choices, the analysis remains:

- Interpretable
- Reproducible
- Defensible

---

## 7. What Comes Next

With the Auto MPG dataset:

- Cleaned
- Loaded correctly
- Visually examined
- Matched to appropriate assumptions

we are now ready to:

→ **Choose algorithms and assumptions**, and  
→ **Begin exploratory and systematic searches**, including Grid Search and model evaluation.

This dataset will be used as a running example throughout the remainder of the workflow pages.