import tkinter as tk
import numpy as np
from sklearn import preprocessing

from scale import Scale
from binarize import Binarize
from normalize import Normalize
from discretize import Discretize

from drow_matrix import DrowMatrix

class Part_1:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title('Предобработка данных')
    self.root.resizable(False, False)

    self.generate_matrix()

    self.asoc_arr = [['yellow', 1], ['black', 3], ['green', 2], ['red', 5], ['white', 4]]

  def generate_matrix(self):
    self.matrix = np.random.rand(5, 5)

  def draw_matrix(self, matrix):
    matrix_frame = tk.Frame(self.root)

    for index_row, row in enumerate(matrix):
      for index_column, column in enumerate(row):
        tk.Label(matrix_frame, text=column, padx=5, pady=5).grid(row=index_row, column=index_column)

    matrix_frame.pack()

  def bin(self):
    Binarize(self.root, self.matrix)
  
  def scaler(self):
    Scale(self.root, self.matrix)

  def norm(self):
    Normalize(self.root, self.matrix)

  def discretizer(self):
    Discretize(self.root, self.matrix)

  def draw_widgets(self):
    tk.Label(self.root, text="Случайно сгенерированная матрица:").pack()

    self.draw_matrix(self.matrix)

    actions_frame = tk.Frame(self.root)

    tk.Button(actions_frame, text="Бинаризация", command=self.bin).pack(side=tk.LEFT)
    tk.Button(actions_frame, text="Масштабирование", command=self.scaler).pack(side=tk.LEFT)
    tk.Button(actions_frame, text="Нормализация", command=self.norm).pack(side=tk.LEFT)
    tk.Button(actions_frame, text="Дискритизация", command=self.discretizer).pack(side=tk.LEFT)
    tk.Button(actions_frame, text="Стандартизация", command=self.standart).pack(side=tk.LEFT)

    actions_frame.pack()

    tk.Label(self.root, text="Ассоциативный массив:").pack()
    self.draw_matrix(self.asoc_arr)

    actions_frame_2 = tk.Frame(self.root)
    tk.Button(actions_frame_2, text="Кодирование", command=self.code).pack(side=tk.LEFT)
    actions_frame_2.pack()

  def standart(self):
    standart_matrix = preprocessing.MaxAbsScaler().fit_transform(self.matrix)
    DrowMatrix(self.root, standart_matrix, 'Предобработка данных - Стандартизация', 'Стандартизированная матрица:')

  def code(self):
    code_asoc_arr = preprocessing.OrdinalEncoder().fit(self.asoc_arr).transform(self.asoc_arr)
    DrowMatrix(self.root, code_asoc_arr, 'Предобработка данных - Кодирование', 'Закодированный асоциативный массив:')

  def run(self):
    self.draw_widgets()
    self.root.mainloop()

if __name__ == '__main__':
  part_1 = Part_1()
  part_1.run()