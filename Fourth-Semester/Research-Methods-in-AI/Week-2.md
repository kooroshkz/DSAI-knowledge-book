- **Frequentist testing steps**
    - Make hypotheses
        - One sided: H0 $\to$ Apple is faster than Xiaomi ($H_0 : \mu_A > \mu_X$)
        - Two sided: H0 $\to$ One of Apple or Xiaomi is faster than the other. ($H_0 : \mu_A \neq \mu_X$)
    - Collect data
    - Calculate statistics
    - Inference
    - Draw conclusions
- **t-test**: number that tells us how far our sample result is from what the null hypothesis expects
    - Standard Error $(SE) = \frac{\sigma}{\sqrt{n}}$
    - $t = \frac{\bar{x} - \mu}{SE} = \frac{\text{observed difference} - \text{expected difference (from } H_0\text{)}}{\text{standard error}}$
    - Where $\bar{x}$ is the sample mean, $\mu$ is the population mean.

- **Tests**:
    - **One-sample t-test**: Checks if the mean of your sample is equal to some specific value.
        - **Null hypothesis**: The average value in the population is equal to a known number.
        - **Formula**: $t = \frac{\bar{x} - \mu_{null}}{SE}$
    - **Chi-squared test for independence**
        - **Null hypothesis**: The two categorical variables are independent.
        - **Formula**: $X^2 = \sum \frac{(Observed - Expect)^2}{E}$
    - **Two-sample t-test for independent samples**
        - **Null hypothesis**: The means of two independent groups are equal.
        - **Formula**: $t = \frac{\bar{x}_1 - \bar{x}_2}{SE}$, where $SE$ is the standard error of the difference between the two means.
    - **Two-sample t-test for paired samples**
        - **Null hypothesis**: The means of two related groups are equal.
        - **Formula**: $t = \frac{\bar{d}}{SE_d}$, where $\bar{d}$ is the mean of the differences and $SE_d$ is the standard error of the differences.
    - **Linear regression**

- **Types of distributions**:
    - **Population distribution**: The distribution of a variable in the entire population.
    - **Sample distribution**: The distribution of a variable in a specific sample.
    - **Sampling distribution**: The distribution of a statistic (like the sample mean) across all possible samples of a given size from the population.

- **Central Limit Theorem**: Sample means form a normal shape, even if the data isn’t normal

- **p-value**: The chance of observing the data (if low chance, we reject null hypothesis)
- **Errors**:
    - **Type I error**: Rejecting the null hypothesis when it is true (false positive).
    - **Type II error**: Failing to reject the null hypothesis when it is false (false negative).
        - **Power**: The probability of correctly rejecting a false null hypothesis (1 - Type II error rate).
        - Chance that a test correctly finds a real effect when there actually is one.

