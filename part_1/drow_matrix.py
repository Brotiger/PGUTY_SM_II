import tkinter as tk
import numpy as np

class DrowMatrix:
  def __init__(self, parent, matrix, title, text=None):
    self.root = tk.Toplevel(parent)
    self.root.title(title)
    self.root.resizable(False, False)

    self.text = text
    self.matrix = matrix

    self.draw_widgets()
    self.grab_focus()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_matrix(self, matrix):
    matrix_frame = tk.Frame(self.root)

    for index_row, row in enumerate(matrix):
      for index_column, column in enumerate(row):
        tk.Label(matrix_frame, text=column, padx=5, pady=5).grid(row=index_row, column=index_column)

    if self.text:
      tk.Label(self.root, text=self.text).pack()
      
    matrix_frame.pack()

  def draw_widgets(self):
    self.draw_matrix(self.matrix)