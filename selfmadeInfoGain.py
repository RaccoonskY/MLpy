
def gini_impurity(value_list):
    if len(value_list) == 0:
        return 0

    all_cases = len(value_list)
    positive_cases = len([x for x in value_list if x == 1])
    negative_cases = all_cases - positive_cases

    if positive_cases == 0 or negative_cases == 0:
        return 0
    else:
        percentage_pos = float(positive_cases / all_cases)
    return 2 * percentage_pos * (1 - percentage_pos)


def information_gain(S, A, B):
    if len(S) == 0:
        return 0
    return gini_impurity(S) - len(A)/len(S) * gini_impurity(A) - len(B)/len(S) * gini_impurity(B)


S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

print(round(information_gain(S, A, B), 5))
