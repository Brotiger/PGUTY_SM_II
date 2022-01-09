import tkinter as tk
from randomForest.randomForest import RandomForest

class RandomForestType:
  def __init__(self, parent):
    self.root = tk.Toplevel(parent)
    self.root.title('Ансамблевое обучение')
    self.root.resizable(False, False)

    self.draw_widgets()
    self.grab_focus()

  def grab_focus(self):
    self.root.grab_set()
    self.root.focus_set()
    self.root.wait_window()

  def draw_widgets(self):
    tk.Button(self.root, text="Классификатор на основе случайного леса", width=60, command=self.rf).pack()
    tk.Button(self.root, text="Классификатор на основе предельно случайного леса", width=60, command=self.rfe).pack()

  def rf(self):
    RandomForest('rf')
  def rfe(self):
    RandomForest('rfe')