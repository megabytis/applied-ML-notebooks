## Confusion Matrix :
    - Confusion matrix is a simple table used to measure how well a classification model is performing.
    - It compares the predictions made by the model with the actual results and shows where the model was right or wrong.
    - This helps us to understand where the model is making mistakes so we can improve it.

- It breaks down the predictions into four categories:-

- **True Positive (TP)** : The model correctly predicted a positive outcome i.e the actual outcome was positive.
- **True Negative (TN)**: The model correctly predicted a negative outcome i.e the actual outcome was negative.
- **False Positive (FP)**: The model incorrectly predicted a positive outcome i.e the actual outcome was negative. It is also known as a Type I error.
- **False Negative (FN)**: The model incorrectly predicted a negative outcome i.e the actual outcome was positive. It is also known as a Type II error.

- The confusion Matrix diagram 👇

|                        | Predicted: Failed (0) | Predicted: Passed (1) |
|------------------------|-----------------------|-----------------------|
| **Actual: Failed (0)** |          TN           |         FP            |
| **Actual: Passed (1)** |          FN           |         TP            |


# Metrics based on Confusion Matrix Data :

## Accuracy-score :
    - Accuracy shows how many predictions the model got right out of all the preictions.
    - It gives the idea of overall performance but it can be mileading when one class is more dominant than the other.
    - For example a model that predicts the majority class correctly most of the time might have high accuracy but still fail to capture important details about other classes

## Precision-score :
    - Precession focus on the quality of the model's postive predictions.
    - It tells us how many of the "positive" predictions were actually correct
    - It is important in situations where false positives need to be minimized such as detecting spam emails or fraud.
    - Formula: TP / (TP + FP)

## Recall-score :
    - Recall measures how good the model is at predicting positives.
    - it shows the proportion of true positive detected out of all the actual posiive instances.
    - High recall is essential when missing postive cases has significant consequenses like in medical tests.
    - Formula: TP / (TP + FN) 

## F1-Score :
    - F1-score combines precission and recall into a single metric to balance their trade-off.
    - It provides a better sense of a model's overall performance particularly for imbalanced datasets.
    - It is helpful when both false positives and false negatives are important though it assumes precision and recall are equally important but in some situations one might matter more than the other.
    - Formula: (2 * Precision * Recall) / (Precision + Recall)