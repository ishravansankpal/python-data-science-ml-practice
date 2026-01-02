# Objective
# Compute and understand basic classification evaluation metrics using a given confusion matrix.

# Problem Description
# Given the values of a confusion matrix:
# - True Positives (TP)
# - False Negatives (FN)
# - False Positives (FP)
# - True Negatives (TN)

# The goal is to compute the following metrics **using their mathematical formulas**:
# - Accuracy
# - Error Rate
# - Precision
# - Recall

# Given Confusion Matrix Values
# - True Positives (TP): 1  
# - False Negatives (FN): 8  
# - False Positives (FP): 1  
# - True Negatives (TN): 90  

# Metrics Computed
# - Accuracy
# - Error Rate
# - Precision
# - Recall

# Approach
# - Each metric is calculated step-by-step using its standard formula.
# - No external machine learning libraries are used.
# - The implementation focuses on clarity and conceptual understanding of evaluation metrics.

# ## Concepts Covered
# - Confusion Matrix
# - Classification Performance Metrics
# - Model Evaluation Fundamentals
  
# Given values
TP = 1
FP = 1
FN = 8
TN = 90

# Formulas
accuracy = (TP + TN) / (TP + TN + FP + FN)
error_rate = 1 - accuracy
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print(f"Accuracy: {accuracy}")
print(f"Error Rate: {error_rate}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

