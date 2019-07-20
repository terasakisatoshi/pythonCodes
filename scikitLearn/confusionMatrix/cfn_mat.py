from sklearn.metrics import confusion_matrix


def main():
    gt_value__ = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    pred_value = [2, 1, 1, 1, 1, 2, 1, 1, 1, 1]
    cnf_mat = confusion_matrix(gt_value__, pred_value)
    print(cnf_mat)
if __name__ == '__main__':
    main()
