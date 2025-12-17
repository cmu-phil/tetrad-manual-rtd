# Model Evaluation and Markov Checking

After running causal searches (including grid searches) and collecting candidate models, the next crucial step is **evaluating those models**.  
This page introduces how to assess whether candidate graphs are consistent with the data — with a focus on the **Markov Checker** and related diagnostics in Tetrad.

Rather than accepting a model at face value, causal analysis should involve **criticism and testing**. The Markov Checker helps answer the question many users really care about:

> **“Is this model even in the ballpark given the data we have?”**

---

## 1. Why Model Evaluation Matters

Causal discovery algorithms output *models that fit certain assumptions and search criteria*. That doesn’t mean they actually *explain the data well*. Some common pitfalls are:

- Overfitting to noise
- Violating observed conditional independences
- Producing complex graphs without empirical support

Model evaluation helps you discriminate between models that are:
- **plausible** given the data, and
- those that are **statistically contradicted** by it.

The Markov Checker is your primary tool for this in Tetrad.

---

## 2. What the Markov Checker Does

Every causal graph entails a set of **conditional independence (CI) relations** via the Markov property. The Markov Checker:

- Takes a candidate graph
- Extracts the implied CI relations
- Tests those implications against the data using appropriate independence tests

If the implied independences are not supported, the model *fails* the Markov check.

### Intuition

Think of the Markov Checker as asking:

> “Given this graph’s structure, we expect certain d-separation relationships. Do we see them in the data?”

If not, then either the assumptions behind the graph are wrong, or the data do not reflect that model.

---

## 3. Running the Markov Checker in Tetrad

To evaluate a model:

1. **Select the estimated graph** in the Graph tab
2. Open the **Markov Checker** utility
3. Choose an independence test that matches your data
    - For continuous data: Fisher-Z, rank-based tests, etc.
    - For discrete data: discrete tests
4. Run the check

Tetrad will report:
- A **summary statistic** for how well the graph’s implied CIs match the data
- A list of *violated* vs *non-violated* implications

---

## 4. Interpreting Markov Checker Output

### Key Outputs

- **Pass/Fail Indicator**
    - Whether the model meets a threshold of consistency
- **Statistic or p-value**
    - How strong the overall evidence is for or against the Markov properties
- **List of Violations**
    - Specific conditional independence statements that do not hold

### What It Means

- **Few or no violations + good statistic**
    - The model is *not ruled out* by conditional independence structure
- **Many violations**
    - The model is likely inconsistent with the observed data
- **Marginal failures**
    - Consider revising assumptions, test choice, or model complexity

---

## 5. Minimal Markov Models

In practice, you often want models that:

1. **Pass the Markov check**, and
2. Are as **simple as possible** (fewest edges or parsimonious parameterization)

This idea of **minimal Markov models** helps guide:
- how you navigate grid search results, and
- how you choose among many passing models.

A model that passes a Markov check but is overly complex may be less useful than a sparser one that also passes.

---

## 6. Comparing Models

When you have multiple candidates from a grid search:

- **Sort or visualize** models by:
    - Markov consistency statistic
    - Number of edges (or degrees of freedom)
    - Stability across tests and parameters
- Look for:
    - **Marked improvements** in consistency
    - **Stable adjacencies/orientations** across models
    - **Trade-offs** where slight complexity increases greatly improve consistency

A typical pattern is:
- very sparse models fail Markov
- very dense models pass but are overly complex
- *somewhere in between* are the minimal models worth reporting

---

## 7. Beyond Markov: Other Diagnostics

While the Markov Checker focuses on conditional independence implications, you can also:

- Use **resampling/stability analysis** (e.g., bootstrap)
    - Identify edges that are consistently recovered
- Compare **alternative tests/scores**
    - See if conclusions change under different assumptions
- Conduct **domain-specific validations**
    - E.g., known causal relations, intervention data

These are advanced but valuable for deep analysis.

---

## 8. Practical Tips

### ✔ Choose a sensible independence test
Match the test to your data type and distribution. Poor test choice can lead to misleading Markov results.

### ✔ Inspect violations closely
Sometimes a few violations arise from sampling noise or borderline effects. Use judgment.

### ✔ Combine with Grid Search
Model evaluation should be integrated with systematic search:
- Use evaluations from each grid search candidate
- Rank models by both **Markov consistency** and **simplicity**

### ✔ Document your decisions
Recording how you evaluated and selected models promotes transparency and reproducibility.

---

## 9. Summary

The Markov Checker is a cornerstone of model evaluation in Tetrad:

- It puts *data-derived constraints* at the center of causal analysis
- It helps separate *plausible* from *implausible* candidate models
- Together with grid search and simplicity considerations, it helps you find **minimal Markov models**

This evaluation step turns causal *search* into causal *inference*.

---

## 🧭 What’s Next

After evaluating models, you should proceed to **Interpreting Results**, which helps you:

- Communicate what features of the graph are justified
- Understand which causal claims are robust
- Distinguish between confirmed structure and uncertainty