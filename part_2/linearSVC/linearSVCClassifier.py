import tkinter as tk
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.model_selection import train_test_split, cross_val_score

class LinearSVCClassifier:
  def __init__(self, parent, path):
    self.root = tk.Toplevel(parent)
    self.root.title('Обучение с учителем')
    self.root.resizable(False, False)

    self.linearSVCClassifier(path)

    #self.draw_widgets()

  def draw_widgets(self):
    #Процент попадания при класификации
    tk.Label(self.root, text=f"Accurancy: {self.accuracy}%").pack()
    tk.Label(self.root, text=f"Precision: {self.precision}%").pack()
    #Сколько удалось класифицировать
    tk.Label(self.root, text=f"Recall: {self.recall}%").pack()
    tk.Label(self.root, text=f"F1: {self.f1}%").pack()
    tk.Button(self.root, text="Построить график", command=self.draw_graphic).pack()

  def linearSVCClassifier(self, path):
    X = []
    y = []

    count_class1 = 0
    count_class2 = 0

    max_datapoints = 25000

    path = 'dataset/income_data.txt'
    with open(path, 'r') as f:
      for line in f.readlines():
        if count_class1 >= max_datapoints and count_class2 >= max_datapoints:
          break
        if '?' in line:
          continue
        
        #Удаляем перенос строки
        data = line.split(',')
        if data[-1].strip() == '<=50K' and count_class1 < max_datapoints:
          X.append(data)
          count_class1 += 1

        if data[-1].strip() == '>50К' and count_class2 < max_datapoints:
          X.append(data)
          count_class2 += 1

    #Преобразование обычного масива в массив numpy для того что бы была возможность применять функции numpy к данному массиву
    X = np.array(X)

    #Преобразование строковых данных в числовые
    #Создаем новый масив размерностью масива X
    X_encoded = np.empty(X.shape)

    label_encoder = []
    #Перебираем элементы первой строки, если элемент целочисленный то все элементы в матрицы следующие под номером столбца i являются целочисленными
    #Копируем их, если не целочисленный то во всех строках элемент в столбце под номером i кодируем
    for i,item in enumerate(X[0]):
      if item.isdigit():
        X_encoded[:, i] = X[:, i]
      else:
        #Для каждого строкого элемента создается свой LabelEncoder который далее кодирует текстовый элемент и возвращает его закодированное представление
        label_encoder.append(preprocessing.LabelEncoder())
        X_encoded[:, i] = label_encoder[-1].fit_transform(X[:, i])

    #Приводим к целочисленному значению все кроме результата
    X = X_encoded[:, :-1].astype(int)
    #Приводим к целочисленному значению результат
    y = X_encoded[:, -1].astype(int)