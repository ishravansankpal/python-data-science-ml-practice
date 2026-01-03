# # Values from the table
# TP = 90
# FN = 210
# FP = 140
# TN = 9560

# # Formulas
# accuracy = (TP + TN) / (TP + TN + FP + FN)
# error_rate = 1 - accuracy
# precision = TP / (TP + FP)
# recall = TP / (TP + FN)

# print(f"Accuracy: {accuracy}")
# print(f"Error Rate: {error_rate}")
# print(f"Precision: {precision}")
# print(f"Recall: {recall}")


TP  = 90
FN = 210
FP = 140
TN = 9560

accuracy = (TP + TN) / (TP + FN + FP + TN)
error_rate = 1 - accuracy
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print('Accuracy: ', accuracy)
print('Error Rate:', error_rate)
print("Precison:", precision)
print('Recall:', recall)
