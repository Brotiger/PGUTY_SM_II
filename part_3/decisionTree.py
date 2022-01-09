import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from utilities import visualize_classifier

class DecisionTree:
  def __init__(self):
    self.decisionTree()

  def decisionTree(self):
    print('Decision trees\n')
    input_file = 'data_decision_trees.txt'
    data = np.loadtxt(input_file, delimiter=',')

    print('Датасет:')
    print(data)

    X, y = data[:, :-1], data[:, -1]

    class_0 = np.array(X[y==0])
    class_1 = np.array(X[y==1])

    plt.figure()
    plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='black',
      edgecolors='black', linewidth=1, marker='x')
    plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='white',
      edgecolors='black', linewidth=1, marker='o')
    plt.title('Input data')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=5)

    params = {'random_state': 6, 'max_depth': 10}
    classifier = DecisionTreeClassifier(**params)
    classifier.fit(X_train, y_train)

    y_test_pred = classifier.predict(X_test)

    class_names = ['Class-0', 'Class-1']
    print("\n" + "#"*40)
    print("\nClassifier performance on training dataset\n")
    print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))
    print("#"*40 + "\n")
    print("#"*40)
    print("\nClassifier performance on test dataset\n")
    print(classification_report(y_test, y_test_pred, target_names=class_names))
    print("#"*40 + "\n")
    print('------------------------')
    #plt.show()
    #visualize_classifier(classifier, X_train, y_train, 'Training dataset')
    #visualize_classifier(classifier, X_test, y_test, 'Test dataset')