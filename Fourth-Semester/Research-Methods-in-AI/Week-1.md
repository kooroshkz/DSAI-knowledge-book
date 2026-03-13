- **Statistics** $\to$ independent variables (features)
- **Machine Learning** $\to$ dependent variable (label/outcome)
- **Simulating data**:
    - Test method performance with known truth
    - Test analysis before having real data
    - Forces you to consider all assumptions
- **Random Variables**:
    - You don’t know its value until you *observe* or *sample* it.
    - The value is not fixed, it can change and depends on some random process.
    - Each value has a probability of happening (based on its distribution).
- **Categorical Variables**: with BarPlots (frequency counts)
    - **Nominal**: Just names, no order (e.g., color, Gender).
        - Can have **Median** and **Mode**.
    - **Ordinal**: ordered categories (e.g., BSc < MSc < PhD rating scales like 1-5 stars).
- **Numerical Variables**:
    - **Interval**: Continuous values with meaningful differences (e.g., temperature, time).
    - **Ratio**: Like interval but with a true zero point. We can multiply and devide (e.g., weight, price).

- For Numerical Variables, **BarPlots** are not appropriate, use **Histograms** or **BoxPlots** instead.
- **Density plots**: Linear curved Histograms, Like moving average.
    - **Kernel Density Plot**: The total area under the curve is 1.
- **Probability Distributions**:
    - **Continuous** $\to$ Use Probability Density Function (PDF) like **Normal Distribution**.
    - **Discrete** $\to$ Use Probability Mass Function (PMF) like **Binomial Distribution**.

- **Bivariate**: describe two variables like **Correlation** unlike univariate.

- **Variance**: Measure of how much the values of a variable differ from the mean.
    - The variance ($s^2$) is the square of the standard deviation ($s$)
    - $s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$
- **Standard Deviation**: Square root of variance, gives a sense of spread in the same units as the data.
- **Cross-table** (Contingency Table): for categorical variables
<table border="1" style="border-collapse: collapse; text-align: center;">
  <tr>
    <th></th>
    <th>fail</th>
    <th>pass</th>
    <th></th>
  </tr>
  <tr>
    <th>cat</th>
    <td>14</td>
    <td>6</td>
    <td>20</td>
  </tr>
  <tr>
    <th>dog</th>
    <td>10</td>
    <td>2</td>
    <td>12</td>
  </tr>
  <tr>
    <th></th>
    <td>24</td>
    <td>8</td>
    <td>32</td>
  </tr>
</table>

- To go from **Sample** to **Population** we make a **t-test**.
    - **t-test**: Compares means of two groups to see if they are significantly different.
    - **ANOVA**: Compares means of three or more groups.
- **Covariance**: Measure of how two variables change together.
    - Positive covariance means they increase together, negative means one increases while the other decreases.
    - $cov_{x,y} = s_{x,y} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$
    - To standardize covariance, we use **Pearson correlation**
        - $r_{x,y} = \frac{cov_{x,y}}{s_x s_y}$
    - Correlation ranges from -1 to 1.

- **Law of Large Numbers (LLN)**: As the sample size increases, the sample mean approaches the population mean.
- **Central Limit Theorem (CLT)**: The distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the population's distribution.