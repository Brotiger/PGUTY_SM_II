import tkinter as tk
from kMeans import KMeansClass

class Part_4:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title('Обучение без учителя')
    self.root.resizable(False, False)

    self.num_clusters = tk.IntVar()
    self.num_clusters.set(5)
    self.n_init = tk.IntVar()
    self.n_init.set(10)

  def run(self):
    self.draw_widgets()
    self.root.mainloop()

  def draw_widgets(self):
    tk.Label(self.root, text='Количество кластеров').pack()
    tk.Entry(self.root, textvariable=self.n_init).pack()
    tk.Label(self.root, text='Количество итераций алгоритма').pack()
    tk.Entry(self.root, textvariable=self.num_clusters).pack()
    tk.Button(self.root, text="Применить", width=20, command=self.get_entry).pack()
    tk.Button(self.root, text="Очистить", width=20, command=self.delete_entry).pack()

  def get_entry(self):
    n_init = self.n_init.get()
    num_clusters = self.num_clusters.get()

    if n_init > 0 and num_clusters > 0:
      KMeansClass(n_init, num_clusters)

  def delete_entry(self):
    self.n_init.set(10)
    self.num_clusters.set(5)

if __name__ == "__main__":
  part_4 = Part_4()
  part_4.run()