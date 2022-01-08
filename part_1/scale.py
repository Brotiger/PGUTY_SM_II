import tkinter as tk
import numpy as np
from sklearn import preprocessing
from drow_matrix import DrowMatrix

class Scale:
  def __init__(self, parent, matrix):
    self.root = tk.Toplevel(parent)
    self.root.title('Предобработка данных - Масштабирование')
    self.root.resizable(False, False)

    self.matrix = matrix
    self.minScale = tk.DoubleVar()
    self.maxScale = tk.DoubleVar()

    self.draw_widgets()
    self.grab_focus()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    tk.Label(self.root, text='MinScale').pack()
    tk.Entry(self.root, textvariable=self.minScale).pack()
    tk.Label(self.root, text='MaxScale').pack()
    tk.Entry(self.root, textvariable=self.maxScale).pack()
    tk.Button(self.root, text="Применить", width=20, command=self.get_entry).pack()
    tk.Button(self.root, text="Очистить", width=20, command=self.delete_entry).pack()

  def get_entry(self):
    minScale = self.minScale.get()
    maxScale = self.maxScale.get()

    if not minScale:
      minScale = 0.0
    if not maxScale:
      maxScale = 0.0

    if maxScale > minScale:
      scale_matrix = preprocessing.MinMaxScaler(feature_range=(minScale, maxScale)).fit_transform(self.matrix)
      DrowMatrix(self.root, scale_matrix, 'Предобработка данных - Масштабирование', 'Масштабированная матрица:')

  def delete_entry(self):
    self.minScale.set(0.0)
    self.maxScale.set(0.0)