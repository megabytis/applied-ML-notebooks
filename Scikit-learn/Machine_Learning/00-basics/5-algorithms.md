# 🧠 Machine Learning Algorithms Cheatsheet

## ✅ Supervised, Unsupervised & Reinforcement Learning

— All Major Algorithms to solve any type of problems

---

## 🎯 SUPERVISED LEARNING ALGORITHMS

_(Used when you have labeled data — input + known output)_

---

### 🔢 REGRESSION ALGORITHMS → Predict Continuous Values

| Algorithm                   | Use Case Example                  | Key Features                                                            |
| --------------------------- | --------------------------------- | ----------------------------------------------------------------------- |
| Linear Regression           | House price, salary prediction    | Simple, interpretable, assumes linear relationship                      |
| Polynomial Regression       | Non-linear trends (growth curves) | Fits curved relationships using polynomial terms                        |
| Ridge Regression            | Multicollinearity in features     | Adds L2 regularization to reduce overfitting                            |
| Lasso Regression            | Feature selection + regression    | Adds L1 regularization — zeros out weak features                        |
| Elastic Net                 | Mix of Ridge + Lasso              | Best for datasets with many correlated features                         |
| Support Vector Regression   | Non-linear regression             | Uses kernels, robust to outliers                                        |
| Decision Tree Regressor     | Sales, temperature prediction     | Easy to visualize, handles non-linearity                                |
| Random Forest Regressor     | High-accuracy ensemble prediction | Reduces overfitting, handles noisy data well                            |
| Gradient Boosting Regressor | Kaggle competitions               | Sequential boosting — often top performer (XGBoost, LightGBM, CatBoost) |

---

### 🏷️ CLASSIFICATION ALGORITHMS → Predict Discrete Labels

| Algorithm                    | Use Case Example                     | Key Features                                                          |
| ---------------------------- | ------------------------------------ | --------------------------------------------------------------------- |
| Logistic Regression          | Spam detection, medical diagnosis    | Outputs probabilities, linear decision boundary                       |
| K-Nearest Neighbors (KNN)    | Image recognition, recommendations   | Instance-based, needs distance metric                                 |
| Naive Bayes                  | Text classification, spam filter     | Fast, works great with text, assumes independence                     |
| Decision Tree Classifier     | Customer churn, loan approval        | Interpretable, handles mixed data types                               |
| Random Forest Classifier     | Credit scoring, disease prediction   | Ensemble of trees — robust and accurate                               |
| Support Vector Machine (SVM) | Image classification, bioinformatics | Powerful in high dimensions, uses kernels                             |
| Gradient Boosting Classifier | High-accuracy classification         | Sequential boosting — wins competitions (XGBoost, LightGBM, CatBoost) |
| Neural Networks (MLP)        | Complex pattern recognition          | Very flexible, needs lots of data & tuning                            |
| SGD Classifier               | Large-scale linear classification    | Efficient for big datasets, supports online learning                  |

---

## 🌀 UNSUPERVISED LEARNING ALGORITHMS

_(Used when you have unlabeled data — only input, no output)_

---

### 🧩 CLUSTERING → Group Similar Data Points

| Algorithm               | Use Case Example                         | Key Features                                      |
| ----------------------- | ---------------------------------------- | ------------------------------------------------- |
| K-Means Clustering      | Customer segmentation, image compression | Simple, fast — must choose K (number of clusters) |
| Hierarchical Clustering | Biology, document clustering             | Builds dendrogram — no need to predefine K        |
| DBSCAN                  | Anomaly detection, spatial data          | Finds dense regions, handles noise & outliers     |
| Gaussian Mixture Models | Soft clustering (probabilistic)          | Assigns probability of belonging to each cluster  |
| Mean Shift Clustering   | Computer vision, object tracking         | Finds modes (peaks) in data density               |
| Affinity Propagation    | Unknown number of clusters               | Message passing — good for small/medium datasets  |

---

### 📉 DIMENSIONALITY REDUCTION → Reduce Features, Keep Info

| Algorithm             | Use Case Example                          | Key Features                                  |
| --------------------- | ----------------------------------------- | --------------------------------------------- |
| PCA                   | Visualization, noise reduction            | Linear — finds directions of maximum variance |
| t-SNE                 | Visualizing embeddings, images            | Non-linear — preserves local structure        |
| UMAP                  | Faster alternative to t-SNE               | Preserves local + global structure, scalable  |
| LDA                   | Classification + dimensionality reduction | Supervised — uses class labels for projection |
| Autoencoders (Neural) | Image compression, anomaly detection      | Deep learning — learns efficient encoding     |

---

### 🛒 ASSOCIATION RULE LEARNING → Find “People who bought X also bought Y”

| Algorithm | Use Case Example         | Key Features                             |
| --------- | ------------------------ | ---------------------------------------- |
| Apriori   | Market basket analysis   | Finds frequent itemsets, generates rules |
| FP-Growth | Faster, scalable Apriori | Uses FP-tree — more memory efficient     |

---

### 🚨 ANOMALY DETECTION → Find Rare / Suspicious Data Points

| Algorithm            | Use Case Example               | Key Features                                |
| -------------------- | ------------------------------ | ------------------------------------------- |
| Isolation Forest     | Fraud detection, monitoring    | Fast, works well with high-dimensional data |
| One-Class SVM        | Manufacturing defect detection | Learns boundary around “normal” data        |
| Local Outlier Factor | Local anomaly detection        | Compares density of point to its neighbors  |

---

## 🎮 REINFORCEMENT LEARNING ALGORITHMS

_(Agent learns by interacting with environment to maximize reward)_

---

### 🤖 VALUE-BASED METHODS → Learn value of actions/states

| Algorithm            | Use Case Example             | Key Features                                       |
| -------------------- | ---------------------------- | -------------------------------------------------- |
| Q-Learning           | Grid worlds, simple games    | Model-free, learns Q-values for state-action pairs |
| Deep Q-Network (DQN) | Atari games, complex control | Uses deep neural nets to approximate Q-function    |
| Double DQN           | Improved DQN                 | Reduces overestimation bias in Q-values            |
| Dueling DQN          | Better value estimation      | Separates state value and advantage estimation     |

---

### 🧬 POLICY-BASED METHODS → Learn policy directly

| Algorithm                               | Use Case Example                | Key Features                                           |
| --------------------------------------- | ------------------------------- | ------------------------------------------------------ |
| REINFORCE                               | Simple policy gradient          | Monte Carlo method — high variance, simple             |
| Actor-Critic                            | Robotics, game AI               | Combines value and policy learning — lower variance    |
| A2C / A3C                               | Parallel training (A3C = async) | Scales well across multiple agents/environments        |
| PPO (Proximal Policy Optimization)      | Robotics, game AI, SOTA RL      | Stable, efficient — widely used in research & industry |
| TRPO (Trust Region Policy Optimization) | High-dimensional control        | Guarantees monotonic improvement — complex math        |

---

### 🔄 MODEL-BASED METHODS → Learn environment dynamics

| Algorithm                      | Use Case Example             | Key Features                                            |
| ------------------------------ | ---------------------------- | ------------------------------------------------------- |
| Dyna-Q                         | Planning + learning          | Combines Q-learning with model simulation               |
| Monte Carlo Tree Search (MCTS) | Game AI (e.g., AlphaGo)      | Uses tree search + random sampling — no training needed |
| Model-Based RL (MBRL)          | Robotics, autonomous systems | Learns transition model — plans ahead efficiently       |

---

### 🧠 HYBRID / ADVANCED METHODS

| Algorithm                                 | Use Case Example             | Key Features                                 |
| ----------------------------------------- | ---------------------------- | -------------------------------------------- |
| SAC (Soft Actor-Critic)                   | Robotics, continuous control | Maximizes entropy — sample efficient, stable |
| TD3 (Twin Delayed DDPG)                   | Continuous action spaces     | Improves DDPG — reduces overestimation       |
| Rainbow DQN                               | Combines 6 DQN improvements  | SOTA for discrete action Atari games         |
| DDPG (Deep Deterministic Policy Gradient) | Robotics, continuous control | Actor-critic for continuous actions          |

---

## 🧭 Quick Algorithm Selection Guide

| Problem Type             | Recommended Algorithms                               |
| ------------------------ | ---------------------------------------------------- |
| Predicting a number?     | Linear/Polynomial Regression, Random Forest, XGBoost |
| Predicting a category?   | Logistic Regression, SVM, Random Forest, XGBoost     |
| Grouping data?           | K-Means, DBSCAN, Hierarchical Clustering             |
| Too many features?       | PCA, t-SNE, UMAP                                     |
| Find buying patterns?    | Apriori, FP-Growth                                   |
| Detect anomalies?        | Isolation Forest, LOF, One-Class SVM                 |
| Agent learning from env? | Q-Learning, DQN, PPO, SAC, A3C                       |

---

📌 **Pro Tip for Beginners**:  
Start simple → Linear/Logistic Regression, K-Means, Q-Learning.  
Then level up → Ensembles (Random Forest, XGBoost), Deep RL (DQN, PPO).

---

🔖 Save this as `ml_algorithms_github.md` — perfect for GitHub repos, documentation, or personal study sheets!
