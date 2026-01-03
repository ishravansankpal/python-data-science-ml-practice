# 22. Compute the Accuracy, Error Rate, Precision, and Recall for the following confusion matrix:

# Out of 10,000 total instances, 230 cases actually have cancer and 9,770 cases do not have cancer.
# Among the cancer cases, 90 are correctly predicted as cancer and 140 are incorrectly predicted as no cancer.
# Among the non-cancer cases, 210 are incorrectly predicted as cancer and 9,560 are correctly predicted as no cancer.

# Values from the table
TP = 90
FN = 210
FP = 140
TN = 9560

# Formulas
accuracy = (TP + TN) / (TP + TN + FP + FN)
error_rate = 1 - accuracy
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print(f"Accuracy: {accuracy}")
print(f"Error Rate: {error_rate}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")




