"""
This program shows example of working with confusion matrix
we calculate accuracy, precision, recall and f1 based on data from CM
"""


tp, fp, fn, tn = [int(x) for x in input().split()]

total = tp + fp + fn + tn
accuracy = (tp + tn) / total
precision = tp/ (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * precision * recall / (precision+recall)

print(round(accuracy, 4))
print(round(precision, 4))
print(round(recall, 4))
print(round(f1_score, 4))


