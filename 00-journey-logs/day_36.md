## 🗓️ Day 36 – 18/10/2025

### 📍 Status: ✅ Completed

---

## ✅ What I did today:

### 📌 Topics Reviewed & Practiced:
- 🔬 **Session 47: ANOVA (Analysis of Variance)**
  - **Introduction:** Understood the core purpose of **ANOVA**: to determine if there are any statistically significant differences between the means of **three or more independent groups** (categories).
  - **F-distribution:** Defined the **F-distribution** and its role as the test statistic for ANOVA, which compares the **variance *between* groups** to the **variance *within* groups** to assess if group differences are greater than random chance.
  - **One-way ANOVA:**
    - Mastered the **Steps** involved in conducting the test (calculating Sum of Squares, Degrees of Freedom, Mean Squares, and the F-statistic).
    - Gained **Geometric Intuition** by visualizing the sources of variance.
    - Reviewed the **Assumptions** (normality, independence of samples, and homogeneity of variances).
    - Worked through a **Python Example** to apply the test.
  - **Post-Hoc Test:** Understood why a significant F-test requires a subsequent **Post-Hoc test** (like Tukey's HSD) to determine *which specific pairs* of groups are significantly different.
  - **T-test Limitation:** Clarified **Why the t-test is not used for more than 3 categories**—it increases the **Type I error rate** (False Positives) with every comparison.
  - **Applications in Machine Learning:** Explored its use in ML for **feature selection** and analyzing the impact of categorical features with multiple levels on a target variable.


---

## 📘 Resources Used:
- 🔗 Notes and videos providing the geometric intuition of partitioning total variance (SST = SSB + SSW).

---

## 🔄 Next Up:
- **Non-Parametric Tests:** Begin studying tests used when ANOVA assumptions (normality, homogeneity of variance) are violated (e.g., Kruskal-Wallis H Test).
- **Two-way ANOVA:** Introduce the concept of analyzing two categorical independent variables simultaneously.

---

## 📝 Reflections:
- ANOVA elegantly solves the multiple comparison problem that plagues repeated t-tests.
- The distinction between the F-test (is *any* difference significant?) and post-hoc tests (which *specific* differences are significant?) is crucial.
- The F-distribution is now understood in a practical, problem-solving context.