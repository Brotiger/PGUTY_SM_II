import tkinter as tk
import numpy as np
from sklearn import preprocessing

import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
from naiveBays.naiveBaysClassifierParams import NaiveBaysClassifieParams
from linearSVC.linearSVCClassifier import LinearSVCClassifier

class Part_2:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title('Обучение с учителем')
    self.root.resizable(False, False)

  def run(self):
    self.draw_widgets()
    self.root.mainloop()

  def draw_widgets(self):
    tk.Button(self.root, text="Наивный баейсовский классификатор", width=50, command=self.naiveBays).pack()
    tk.Button(self.root, text="Классификатор на основе машины опорных векторов", width=50, command=self.linearSVC).pack()

  def naiveBays(self):
    NaiveBaysClassifieParams(self.root)

  def linearSVC(self):
    LinearSVCClassifier()

if __name__ == "__main__":
  part_2 = Part_2()
  part_2.run()