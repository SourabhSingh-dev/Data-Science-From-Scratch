## 🗓️ Day 33 – 16/10/2025

### 📍 Status: ✅ Completed

---

## ✅ What I did today:

### 📌 Topics Reviewed & Practiced:
- 🎯 **Session 44: Confidence Intervals (CI)**
  - **Foundations:** Solidified the distinction between **Population vs. Sample** and **Parameter vs. Estimate**. Defined a **Point Estimate** as a single best guess for a parameter.
  - **Confidence Interval (CI):**
    - Understood CI as a range of values likely to contain the true population parameter.
    - Reviewed the **Applications of CI** (e.g., reporting survey results, quality control).
    - Learned the **Ways to calculate CI** and the **Assumptions** and **Intuition of the z-procedure**.
    - Mastered the **Interpretation of CI** (e.g., "We are 95% confident the true mean lies between X and Y").
    - Explored the **T-procedure and t-distribution** as necessary alternatives when the sample size is small or the population standard deviation ($\sigma$) is unknown.
    - Practiced calculating **Confidence Intervals in code**.

---

- 📝 **Session 45: Hypothesis Testing (Part 1)**
  - **Key Idea:** Began the formal study of **Hypothesis Testing** as a procedure for making inferences about a population parameter based on sample data.
  - **Core Components:** Defined the **Null ($\text{H}_0$) and Alternate ($\text{H}_1$) Hypothesis**.
  - **Testing Procedure:** Reviewed the formal **Steps in Hypothesis Testing**.
  - **Z-Test:** Focused on **Performing the z-test** and defining the **Rejection Region and Significance Level** ($\alpha$).
  - **Errors & Tails:** Mastered the distinction between **Type-I ($\alpha$) and Type-II ($\beta$) Error** and the difference between **One-tailed vs. Two-tailed tests**.
  - **Applications:** Explored **Applications of Hypothesis Testing** in general statistics and its specific relevance to **Hypothesis Testing in Machine Learning** (e.g., A/B testing, evaluating model coefficients).

---

## 🧩 Practice & Execution:
-Coded mathematical transformation and power transformation.
- Box-Cox and yeo johnson implementation.

---

## 📘 Resources Used:
- 💻 Jupyter Notebook for CI and initial z-test implementations.
- 🔗 Notes on the $\text{t-distribution}$ and its heavier tails compared to the Normal distribution.

---

## 🔄 Next Up:
- **Hypothesis Testing (Part 2):** Complete the Hypothesis Testing workflow, focusing on P-values, t-tests, and practical application.
- **T-Test Deep Dive:** Implement the t-test from scratch in code to test the significance of model coefficients.

---

## 📝 Reflections:
- Confidence Intervals and Hypothesis Testing are two sides of the same coin; one estimates a range, the other tests a claim.
- The **t-distribution** is a simple but vital conceptual step away from the Normal distribution when sample uncertainty is high.
- The foundation for statistical inference in ML is now robust.