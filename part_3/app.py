import tkinter as tk
import numpy as np
from sklearn import preprocessing

import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
from linearRegression import LinearRegression
from multilinearRegression import MultiLinearRegression
from decisionTree import DecisionTree

class Part_3:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title('Ансамблевое обучение')
    self.root.resizable(False, False)

  def run(self):
    self.draw_widgets()
    self.root.mainloop()

  def draw_widgets(self):
    tk.Button(self.root, text="Классификатор на основе линейного регрессионного алгоритма", width=70, command=self.linearRegression).pack()
    tk.Button(self.root, text="Классификатор на основе многомерного регрессионного алгоритма", width=70, command=self.multiLinearRegression).pack()
    tk.Button(self.root, text="Классификатор на основе дерева решений", width=70, command=self.decisionTree).pack()
    tk.Button(self.root, text="Классификаторы на основе случайного леса и предельно случайного леса", width=70).pack()

  def linearRegression(self):
    LinearRegression()

  def multiLinearRegression(self):
    MultiLinearRegression()

  def decisionTree(self):
    DecisionTree()

if __name__ == "__main__":
  part_3 = Part_3()
  part_3.run()