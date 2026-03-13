### Explanation of Notations and Signs

#### **Confidence Intervals (CIs)**  

1. **General Form**:

$$\text{Point Estimate} \pm \text{Margin of Error}$$

- **Point Estimate**: The sample statistic (e.g., sample mean $\bar{y}$ or sample proportion $\hat{\pi}$).
   - **Margin of Error**: Represents the range around the point estimate capturing uncertainty.

$$\text{Margin of Error} = \text{Score} \times \text{Standard Error}$$

2. **Proportion CI**:  
   - **Standard Error**:

$$\sigma_{\hat{\pi}} = \sqrt{\frac{\pi(1-\pi)}{n}}$$

- $\pi$: True population proportion (if known).
     - $\hat{\pi}$: Sample proportion (used for estimation).  
     - $n$: Sample size.  
     - Estimated as:

$$s.e. = \sqrt{\frac{\hat{\pi}(1-\hat{\pi})}{n}}$$

- **CI Formula**:

$$\hat{\pi} \pm z \cdot s.e.$$

- $z$: Z-score corresponding to the confidence level (e.g., 1.96 for 95%).

3. **Mean CI**:  
   - **Standard Error**:

$$\sigma_{\bar{y}} = \frac{\sigma}{\sqrt{n}}$$

- $\sigma$: Population standard deviation.  
     - $n$: Sample size.  
   - If $\sigma$ is unknown, use:

$$s.e. = \frac{s}{\sqrt{n}}$$

- $s$: Sample standard deviation.

---

#### **t-Distribution**  
- **Use Case**: When the sample size is small ($n < 30$) or $\sigma$ (population standard deviation) is unknown.  
- **Characteristics**:  
  - Similar to the normal distribution but with **thicker tails** (more variability).  
  - As $n$ increases, the t-distribution approaches the normal distribution.  
- **Degrees of Freedom**:

$$df = n - 1$$

- Reflects the amount of information in the sample.

---

### **Choosing Sample Size**  

1. **For Proportions**:

$$n = \frac{\hat{\pi}(1-\hat{\pi}) \cdot z^2}{M^2}$$

- $\hat{\pi}$: Estimated proportion.  
   - $z$: Z-score for desired confidence level.  
   - $M$: Desired margin of error.

2. **For Means**:

$$n = \frac{s^2 \cdot z^2}{M^2}$$

- $s$: Sample standard deviation (estimate for $\sigma$).  
   - $z$: Z-score for desired confidence level.  
   - $M$: Desired margin of error.