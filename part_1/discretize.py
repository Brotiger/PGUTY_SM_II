import tkinter as tk
import numpy as np
from sklearn import preprocessing
from drow_matrix import DrowMatrix

class Discretize:
  def __init__(self, parent, matrix):
    self.root = tk.Toplevel(parent)
    self.root.title('Предобработка данных - Дискретизация')
    self.root.resizable(False, False)

    self.matrix = matrix
    self.n_bins = tk.IntVar()
    self.n_bins.set(2)
    self.strategy = tk.StringVar()

    self.draw_widgets()
    self.grab_focus()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    tk.Label(self.root, text='n_bins (n_bins >= 2)').pack()
    tk.Entry(self.root, textvariable=self.n_bins).pack()
    tk.Label(self.root, text='Strategy').pack()

    self.defaultRadio = tk.Radiobutton(self.root, text="uniform", variable=self.strategy, value="uniform")
    self.defaultRadio.select()
    self.defaultRadio.pack()

    tk.Radiobutton(self.root, text="quantile", variable=self.strategy, value="quantile").pack()
    tk.Radiobutton(self.root, text="kmeans", variable=self.strategy, value="kmeans").pack()

    tk.Button(self.root, text="Применить", width=20, command=self.get_entry).pack()
    tk.Button(self.root, text="Очистить", width=20, command=self.delete_entry).pack()

  def get_entry(self):
    strategy = self.strategy.get()
    n_bins = self.n_bins.get()

    if strategy:
      if n_bins and n_bins >= 2:
        discret_matrix = preprocessing.KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy=strategy).fit(self.matrix).transform(self.matrix)
        DrowMatrix(self.root, discret_matrix, 'Предобработка данных - Дискретизация')

  def delete_entry(self):
    self.defaultRadio.select()
    self.n_bins.set(2)