import tkinter as tk
import numpy as np
from sklearn import preprocessing
from drow_matrix import DrowMatrix

class Normalize:
  def __init__(self, parent, matrix):
    self.root = tk.Toplevel(parent)
    self.root.title('Предобработка данных - Нормализация')
    self.root.resizable(False, False)

    self.matrix = matrix
    self.norm = tk.StringVar()

    self.draw_widgets()
    self.grab_focus()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    tk.Label(self.root, text='Norm').pack()

    self.defaultRadio = tk.Radiobutton(self.root, text="l1", variable=self.norm, value="l1")
    self.defaultRadio.select()
    self.defaultRadio.pack()

    tk.Radiobutton(self.root, text="l2", variable=self.norm, value="l2").pack()
    tk.Button(self.root, text="Применить", width=20, command=self.get_entry).pack()
    tk.Button(self.root, text="Очистить", width=20, command=self.delete_entry).pack()

  def get_entry(self):
    norm = self.norm.get()
    if norm:
      normalized_matrix = preprocessing.normalize(self.matrix, norm=norm)
      DrowMatrix(self.root, normalized_matrix, 'Предобработка данных - Нормализация', 'Нормализованная матрица:')

  def delete_entry(self):
    self.defaultRadio.select()