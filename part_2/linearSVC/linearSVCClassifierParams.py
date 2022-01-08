import tkinter as tk
import numpy as np
from sklearn import preprocessing

import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score

from services.utilities import visualize_classifier
from linearSVC.linearSVCClassifier import LinearSVCClassifier

class LinearSVCClassifierParams:
  def __init__(self, parent):
    self.root = tk.Toplevel(parent)
    self.root.title('Обучение с учителем')
    self.root.resizable(False, False)

    self.path = tk.StringVar()

    self.draw_widgets()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    tk.Label(self.root, text="Абсолютный путь до файла с датасетом").pack()
    tk.Entry(self.root, textvariable=self.path).pack()

    tk.Button(self.root, text="Применить", width=20, command=self.get_entry).pack()
    tk.Button(self.root, text="Очистить", width=20, command=self.delete_entry).pack()

  def get_entry(self):
    path = self.path.get()

    if path:
      LinearSVCClassifier(self.root, path)

  def delete_entry(self):
    self.path.set('')