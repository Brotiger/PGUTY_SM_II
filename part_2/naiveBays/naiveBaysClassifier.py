import tkinter as tk
import numpy as np
from sklearn import preprocessing

import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score

from services.utilities import visualize_classifier
import os

class NaiveBaysClassifie:
  def __init__(self, parent, train):
    self.root = tk.Toplevel(parent)
    self.root.title('Обучение с учителем')
    self.root.resizable(False, False)

    self.naiveBaysClassifier(train)
    self.draw_widgets()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    #Процент попадания при класификации
    tk.Label(self.root, text=f"Accurancy: {self.accuracy}%").pack()
    tk.Label(self.root, text=f"Precision: {self.precision}%").pack()
    #Сколько удалось класифицировать
    tk.Label(self.root, text=f"Recall: {self.recall}%").pack()
    tk.Label(self.root, text=f"F1: {self.f1}%").pack()
    tk.Button(self.root, text="Построить график", command=self.draw_graphic).pack()

  def naiveBaysClassifier(self, train):
    path = 'data_multivar_nb.txt'
    data = np.loadtxt(path, delimiter=',')
    print('Датасет:')
    print(data)
    print('------------------------')

    # 1) : - с какой по какую строку - в нашем случае с первой до последней, 2) : - с какой по какой столбец
    X, y = data[:, :-1], data[:, -1]

    self.X = X
    self.y = y

    num_folds = 3

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train, random_state=num_folds)
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    self.classifier = classifier

    #Проверяем классификацию
    y_test_pred = classifier.predict(X_test)
    
    #shape возвращает количество строк и столбцов
    # (y == y_pred) - формирует матрицу соответствия y и y_pred состоящую из True и False, sum считает количество элементов True
    #accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
    #Accuracy - Точность
    
    accuracy_values = cross_val_score(classifier, X, y, scoring='accuracy', cv=num_folds)
    self.accuracy = round(100*accuracy_values.mean(), 2)
    
    precision_values = cross_val_score(classifier, X, y, scoring='precision_weighted', cv=num_folds)
    self.precision = round(100*precision_values.mean(), 2)

    recall_values = cross_val_score(classifier, X, y, scoring='recall_weighted', cv=num_folds)
    self.recall = round(100*recall_values.mean(), 2)
    
    f1_values = cross_val_score(classifier, X, y, scoring='f1_weighted', cv=num_folds)
    self.f1 = round(100*f1_values.mean(), 2)
  
  def draw_graphic(self):
    visualize_classifier(self.classifier, self.X, self.y)