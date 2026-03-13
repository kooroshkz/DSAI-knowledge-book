## Machine Learning - Lecture 1

### **Machine Learning's Core Ingredients**
- **Tasks** define the problem machine learning is trying to solve. (Predictive vs. Descriptive).
  - **A. Predictive Tasks (Supervised Learning: Help predict next data)**
    - **Classification**
    - **Regression**
    - **Predictive Clustering**

  - **B. Descriptive Tasks (Unsupervised Learning: Help find hidden patterns)**
    - **Descriptive Clustering** → Groups data into clusters which is not known beforehand.
      - Example: Customer segmentation, plant species grouping.
    - **Association Rule Mining** → Identifies relationships between variables.  
      - Example: Market basket analysis (if a person buys bread, they might buy butter).
    - **Subgroup Discovery** → Finds interesting patterns within a specific class of data.  
      - Example: Detecting risk groups for diseases.

Rule mining vs subgroup discovery:
- **Rule Mining** → Generalizes rules across the entire dataset.
- **Subgroup Discovery** → Focuses on specific subgroups within the data.

|                   | *Predictive model*                | *Descriptive model*                          |
|-------------------|---------------------------------|---------------------------------------------|
| *Supervised learning*   | Classification, Regression  | Subgroup discovery                         |
| *Unsupervised learning* | Predictive clustering      | Descriptive clustering, Association rule discovery |

  - **A. Model Categorization by Intuition**
    - **Geometric Models** → Use distances, transformations, and hyperplanes.
      - Example: **Linear regression, SVM**.
    - **Probabilistic Models** → Use probability distributions to reduce uncertainty.
      - Example: **Naïve Bayes**.
    - **Logical Models** → Use interpretable rules for decision-making.
      - Example: **Decision Trees**.

  - **B. Model Categorization by Mode of Operation (modus operandi)**
    - **Grouping Models** → Divide instance space into segments.  
      - Example: **Decision Trees**.
    - **Grading Models** → Learn a single global function over all instances.  
      - Example: **SVM, Linear Regression**.

  - **C. Model Phases**
    - **Training Phase** → The model learns from data.
    - **Inference Phase** → The trained model makes predictions on new data.
    - **Training takes longer than inference** due to learning complexity.

- **Features**
  - **Feature Engineering**
    - **Feature Construction** → Creating features from raw data.
    - **Discretization** → Converting numerical data into categorical bins.
    - **Feature Transformation** → Mapping data into a new space (e.g., PCA).
    - **Feature Selection** → Removing redundant or irrelevant features.

  - **Feature Extraction for Different Data Types**
    - **Images** → Textures, color distribution.
    - **Text** → Word frequencies, TF-IDF.
    - **Time Series** → Maximum, minimum, trends.
