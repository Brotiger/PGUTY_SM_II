import tkinter as tk
import numpy as np
from sklearn import preprocessing
from drow_matrix import DrowMatrix

class Binarize:
  def __init__(self, parent, matrix):
    self.root = tk.Toplevel(parent)
    self.root.title('Предобработка данных - Бинаризация')
    self.root.resizable(False, False)

    self.matrix = matrix
    self.threshold = tk.DoubleVar()

    self.draw_widgets()
    self.grab_focus()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    tk.Label(self.root, text='Threshold').pack()
    tk.Entry(self.root, textvariable=self.threshold).pack()
    tk.Button(self.root, text="Применить", width=20, command=self.get_entry).pack()
    tk.Button(self.root, text="Очистить", width=20, command=self.delete_entry).pack()

  def get_entry(self):
    threshold = self.threshold.get()

    if not threshold:
      threshold = 0.0

    binarized_matrix = preprocessing.Binarizer(threshold=threshold).transform(self.matrix)
    binarized_matrix = binarized_matrix.astype(int)
    DrowMatrix(self.root, binarized_matrix, 'Предобработка данных - Бинаризация', 'Бинаризированная матрица:')

  def delete_entry(self):
    self.threshold.set(0.0)