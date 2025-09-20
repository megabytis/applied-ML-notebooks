# 🧠 Machine Learning Algorithms Cheatsheet

## ✅ Supervised & Unsupervised Learning — All Major Algorithms

---

## 🎯 SUPERVISED LEARNING ALGORITHMS

_(Used when you have labeled data — input + known output)_

---

### 1️⃣ Regression Algorithms

→ Predict **continuous numerical values**

| Algorithm                                                     | Use Case Example                        | Key Features                                             |
| ------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------- |
| **Linear Regression**                                         | House price, salary prediction          | Simple, interpretable, assumes linear relationship       |
| **Polynomial Regression**                                     | Non-linear trends (e.g., growth curves) | Fits curved relationships using polynomial terms         |
| **Ridge Regression**                                          | When multicollinearity exists           | Adds L2 regularization to prevent overfitting            |
| **Lasso Regression**                                          | Feature selection + regression          | Adds L1 regularization — can shrink coefficients to zero |
| **Elastic Net**                                               | Mix of Ridge + Lasso                    | Good when you have many correlated features              |
| **Support Vector Regression (SVR)**                           | Non-linear regression with margins      | Uses kernels, robust to outliers                         |
| **Decision Tree Regressor**                                   | Predict sales, temperature              | Easy to visualize, handles non-linearity                 |
| **Random Forest Regressor**                                   | Ensemble of trees — high accuracy       | Reduces overfitting, handles noise well                  |
| **Gradient Boosting Regressor (XGBoost, LightGBM, CatBoost)** | Winning solution in Kaggle              | Sequential boosting — high performance                   |

---

### 2️⃣ Classification Algorithms

→ Predict **discrete categories / labels**

| Algorithm                                                      | Use Case Example                       | Key Features                                                       |
| -------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------ |
| **Logistic Regression**                                        | Spam detection, medical diagnosis      | Probabilistic output, linear decision boundary                     |
| **K-Nearest Neighbors (KNN)**                                  | Image recognition, recommender systems | Simple, instance-based, needs distance metric                      |
| **Naive Bayes**                                                | Text classification, spam filter       | Fast, works well with text, assumes feature independence           |
| **Decision Tree Classifier**                                   | Customer churn, loan approval          | Interpretable, handles mixed data types                            |
| **Random Forest Classifier**                                   | Credit scoring, disease prediction     | Ensemble of trees — robust, handles overfitting                    |
| **Support Vector Machine (SVM)**                               | Image classification, bioinformatics   | Powerful for high-dim data, uses kernels for non-linear separation |
| **Gradient Boosting Classifier (XGBoost, LightGBM, CatBoost)** | High-accuracy classification           | Sequential boosting, often wins competitions                       |
| **Neural Networks (MLP)**                                      | Complex pattern recognition            | Flexible, needs lots of data & tuning                              |
| **Stochastic Gradient Descent (SGD) Classifier**               | Large-scale linear classification      | Efficient for big datasets                                         |

---

## 🌀 UNSUPERVISED LEARNING ALGORITHMS

_(Used when you have unlabeled data — only input, no output)_

---

### 1️⃣ Clustering Algorithms

→ Group similar data points together

| Algorithm                         | Use Case Example                                | Key Features                                                 |
| --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| **K-Means Clustering**            | Customer segmentation, image compression        | Simple, fast, needs to choose K (number of clusters)         |
| **Hierarchical Clustering**       | Biology (species grouping), document clustering | Builds tree of clusters (dendrogram), no need to predefine K |
| **DBSCAN**                        | Anomaly detection, spatial data                 | Finds dense regions, handles noise & outliers well           |
| **Gaussian Mixture Models (GMM)** | Soft clustering (probabilistic)                 | Assigns probability of belonging to each cluster             |
| **Mean Shift Clustering**         | Computer vision, tracking objects               | Finds modes (peaks) in data density                          |
| **Affinity Propagation**          | When you don’t know number of clusters          | Uses message passing, good for small/medium datasets         |

---

### 2️⃣ Dimensionality Reduction Algorithms

→ Reduce number of features while preserving information

| Algorithm                              | Use Case Example                                          | Key Features                                                  |
| -------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------- |
| **Principal Component Analysis (PCA)** | Visualization, noise reduction                            | Linear, finds directions of max variance                      |
| **t-SNE**                              | Visualizing high-dim data (e.g., images, word embeddings) | Non-linear, great for 2D/3D plots — preserves local structure |
| **UMAP**                               | Faster alternative to t-SNE                               | Preserves both local and global structure, scalable           |
| **Linear Discriminant Analysis (LDA)** | Classification + dimensionality reduction                 | Supervised — uses class labels to find best projection        |
| **Autoencoders (Neural)**              | Image compression, anomaly detection                      | Deep learning-based, learns efficient encoding                |

---

### 3️⃣ Association Rule Learning

→ Find relationships between variables (e.g., “customers who buy X also buy Y”)

| Algorithm             | Use Case Example              | Key Features                                         |
| --------------------- | ----------------------------- | ---------------------------------------------------- |
| **Apriori Algorithm** | Market basket analysis        | Finds frequent itemsets, generates association rules |
| **FP-Growth**         | Faster alternative to Apriori | Uses tree structure, more memory efficient           |

---

### 4️⃣ Anomaly Detection (Often Unsupervised)

→ Find rare or unusual data points

| Algorithm                      | Use Case Example                          | Key Features                           |
| ------------------------------ | ----------------------------------------- | -------------------------------------- |
| **Isolation Forest**           | Fraud detection, system health monitoring | Fast, works well with high-dim data    |
| **One-Class SVM**              | Detect outliers in manufacturing          | Learns boundary around “normal” data   |
| **Local Outlier Factor (LOF)** | Detect local anomalies                    | Compares density of point to neighbors |

---

## 🧭 Quick Decision Guide

✅ **Want to predict a number?** → Use **Regression** algorithms  
✅ **Want to predict a category?** → Use **Classification** algorithms  
✅ **Want to group data?** → Use **Clustering**  
✅ **Want to reduce features?** → Use **Dimensionality Reduction**  
✅ **Want to find buying patterns?** → Use **Association Rules**  
✅ **Want to find weird/fraudulent data?** → Use **Anomaly Detection**

---

📌 **Pro Tip**:  
Start simple → Try Linear/Logistic Regression or K-Means first.  
Then scale up → Use ensemble methods (Random Forest, XGBoost) or deep learning if needed.

---

🔖 Save this as `ml_algorithms_cheatsheet.md` — perfect for quick revision before interviews, exams, or projects!
