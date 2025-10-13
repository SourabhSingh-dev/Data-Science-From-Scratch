## 🗓️ Day 31 – 13/10/2025

### 📍 Status: ✅ Completed

---

## ✅ What I did today:

### 📌 Topics Reviewed & Practiced:
- 🔔 **Session 41: Normal Distribution (Gaussian Distribution)**
  - **PDF in Data Science:** Solidified the understanding of how Probability Density Functions are used to model the likelihood of continuous data points, particularly for inference and feature engineering.
  - **2D Density Plots:** Explored the visualization of joint probability distributions between two variables using 2D density plots.
  - **Normal Distribution Deep Dive:**
    - **Importance, Equation, Parameters ($\mu$ and $\sigma$):** Understood why the Normal Distribution is central to statistics and machine learning (Central Limit Theorem).
    - **Properties:** Reviewed key characteristics like symmetry, the total area under the curve summing to one, and how the mean, median, and mode coincide.
  - **Standard Normal Variate (Z-Score):**
    - Understood the importance of standardization (Z-score calculation: $Z = \frac{x - \mu}{\sigma}$) to transform any Normal Distribution into the standard distribution ($\mu=0, \sigma=1$).
    - Practiced using the **Z-table** to find probabilities.
    - Applied the **Empirical Rule (68-95-99.7)** for quick probability estimations.
  - **Skewness:** Related Skewness back to the shape of the Normal Distribution (which has zero skewness).
  - **CDF of Normal Distribution:** Used the Cumulative Distribution Function (CDF) and Z-scores to calculate cumulative probabilities, which are essential for statistical hypothesis testing.

---

## 🧩 Practice & Execution:
- 💻 **Code Implementation:** Wrote Python code using `numpy` and `scipy.stats` to:
  - Generate normally distributed random data with custom $\mu$ and $\sigma$.
  - **Visualize** the bell curve using the PDF equation and demonstrate the effects of changing $\mu$ and $\sigma$.
- **Data Science Use Cases:** Practiced applying the Z-score and Empirical Rule for **outlier detection** and **data normalization** (scaling features for models).

---

## 📘 Resources Used:
- 🧪 Jupyter Notebook for all code implementations and visualizations.
-    Iris and Titanic dataset.
- 📊 Notes and online resources for Z-table practice.

---

## 🔄 Next Up:
- **Other Key Distributions:** Move on to studying the **Bernoulli and Binomial Distributions** (Discrete Distributions).
- Understand the parameters and practical applications of these discrete distributions, particularly in classification problems.

---

## 📝 Reflections:
- The Normal Distribution is clearly the bedrock of inferential statistics in ML. Standardizing with the Z-score makes diverse datasets comparable.
- Coding the concepts (especially using `scipy.stats.norm.cdf`) was very effective for cementing the intuition behind the Z-table.
- Ready to shift focus to discrete probability distributions next.