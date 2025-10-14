## 🗓️ Day 32 – 14/10/2025

### 📍 Status: ✅ Completed

---

## ✅ What I did today:

### 📌 Topics Reviewed & Practiced:
- 📉 **Session 42: Non-Gaussian Probability Distributions & Data Shape**
  - **Kurtosis:** Defined Kurtosis as a measure of the "tailedness" and peakedness of a probability distribution.
  - **Excess Kurtosis & Types:** Understood the concept of Excess Kurtosis and the classification of distributions into:
    - **Mesokurtic** (Normal distribution, Excess Kurtosis = 0).
    - **Leptokurtic** (Heavy tails, higher peak).
    - **Platykurtic** (Light tails, flatter peak).
  - **QQ Plot (Quantile-Quantile Plot):** Learned to use the QQ plot as a crucial visual tool to determine if a dataset follows a specific distribution (e.g., Normal Distribution) by comparing its quantiles to theoretical quantiles.
  - **Non-Gaussian Distributions:** Reviewed the properties and use cases of non-normal distributions:
    - **Uniform Distribution** (Equal probability across a range).
    - **Log-normal Distribution** (Data whose logarithm is normally distributed).
    - **Pareto Distribution** (The "80/20" rule, power-law distribution).
  - **Transformations (Theory Only):** Reviewed the mathematical and conceptual foundation of various data transformations aimed at achieving a more Gaussian shape:
    - Mathematical Transformations (Log, Reciprocal, Square/Sqrt).
    - Scikit-learn's `FunctionTransformer`.
    - Power Transformations (Box-Cox and Yeo-Johnson).

---

## 🧩 Practice & Execution:
- 💻 **QQ Plot Implementation:** Successfully implemented Python code to generate **QQ plots** for data sampled from various distributions (Normal, Uniform, etc.) to visually assess normality.
- **Interpretation Practice:** Practiced interpreting the characteristic curves of data that deviates from the straight line on the QQ plot (e.g., how heavy tails or skewness appear).
- **Theoretical Review:** Focused heavily on the *why* behind data transformations (to meet assumptions of certain models like Linear Regression).

---

## 📘 Resources Used:
- 🧪 Jupyter Notebook for `scipy.stats` and `statsmodels.api` code practice (QQ plots).
- 📄 Session notes detailing the formulas and practical limits of the various Power Transformations.

---

## 🔄 Next Up:
- **Data Transformation Implementation:** Dedicate the next session to implementing and visually comparing the effects of **Box-Cox** and **Yeo-Johnson** transformations using Python on real-world skewed data.

---

## 📝 Reflections:
- The QQ plot is an indispensable tool for data preprocessing and validating model assumptions.
- Understanding Kurtosis complements Skewness, giving a full picture of the data's shape.
- Must ensure time is allocated tomorrow to code the transformations—theory is clear, but seeing the code's impact is essential.