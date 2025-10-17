## 🗓️ Day 35 – 17/10/2025

### 📍 Status: ✅ Completed

---

## ✅ What I did today:

### 📌 Topics Reviewed & Practiced:
- ✍️ **Session 46: Hypothesis Testing (Part 2) - P-value and T-tests**
  - **P-value Mastery:** Defined the **P-value** as the probability of observing data as extreme as, or more extreme than, the sample data, assuming the null hypothesis ($\text{H}_0$) is true.
  - **Interpretation:** Practiced **Interpreting the P-value** against the significance level ($\alpha$); if $P < \alpha$, we reject $\text{H}_0$.
  - **P-value in Z-test:** Understood how the P-value is calculated in the context of the Z-test.
  - **T-test Deep Dive:** Explored the **T-test** as the primary method for testing means when the population standard deviation ($\sigma$) is unknown (which is common in real-world scenarios).
  - **Types of T-test:** Mastered the three main types:
    - **Single-sample t-Test** (comparing a sample mean to a known population mean).
    - **Independent 2-sample t-Test** (comparing means of two unrelated groups).
    - **Paired 2-sample t-Test** (comparing means of the same group before and after an intervention).

---

- 🔀 **Chi-square test**
  - **Chi-square Distribution:** Reviewed the **Definition and Properties** of the $\chi^2$ distribution.
  - **Chi-square Test:** Defined the **Chi-square test** and its main applications:
    - **Goodness of fit test:** Tested whether an observed frequency distribution significantly differs from a theoretical distribution (e.g., Uniform, Binomial).
    - **Test for Independence:** Determined if there is a statistically significant association between two categorical variables.
  - **ML Applications:** Explored its **Applications in machine learning**, primarily for **feature selection** involving categorical data.


---

## 📘 Resources Used:
- 🔗 `scipy.stats` documentation for t-test functions and $\chi^2$ calculations.

---

## 🔄 Next Up:
- **ANOVA (Analysis of Variance):** Move to testing the means of **more than two groups**.
- **Non-Parametric Tests:** Begin studying non-parametric alternatives when the assumption of normality is violated.

---

## 📝 Reflections:
- The P-value is the final, practical step in the hypothesis testing framework.
- The **Chi-square test** fills a major gap by providing a statistical tool for categorical data, which is essential for ML.
- I now have a comprehensive toolkit for comparing means (Z-test, T-test) and analyzing relationships between categorical variables ($\chi^2$).