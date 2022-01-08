import tkinter as tk
import numpy as np
from sklearn import preprocessing

import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score

from services.utilities import visualize_classifier
from naiveBays.naiveBaysClassifier import NaiveBaysClassifie

class NaiveBaysClassifieParams:
  def __init__(self, parent):
    self.root = tk.Toplevel(parent)
    self.root.title('Обучение с учителем')
    self.root.resizable(False, False)

    self.train = tk.DoubleVar()
    self.path = tk.StringVar()
    self.train.set(0.5)

    self.draw_widgets()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    tk.Label(self.root, text="Абсолютный путь до файла с датасетом").pack()
    tk.Entry(self.root, textvariable=self.path).pack()
    tk.Label(self.root, text="Процент данных для обучения").pack()
    tk.Entry(self.root, textvariable=self.train).pack()

    tk.Button(self.root, text="Применить", width=20, command=self.get_entry).pack()
    tk.Button(self.root, text="Очистить", width=20, command=self.delete_entry).pack()

  def get_entry(self):
    train = self.train.get()
    path = self.path.get()

    if train and train < 1.0 and path:
      NaiveBaysClassifie(self.root, train, path)

  def delete_entry(self):
    self.train.set(0.5)
    self.path.set('')