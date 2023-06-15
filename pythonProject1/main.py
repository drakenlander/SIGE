import tkinter as tk
from tkinter import ttk
import matplotlib
import charts

matplotlib.use('TkAgg')

font = ("Verdana", 35)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        label = ttk.Label(self, text="Sistema de Información de Graduados y Egresados", font=font)
        label.grid(row=0, column=2, padx=10, pady=10)

        button1 = ttk.Button(self, text="Bar Chart", command=lambda: charts.barChart())
        button1.grid(row=1, column=2, padx=10, pady=10)

        button2 = ttk.Button(self, text="Stacked Bar Chart", command=lambda: charts.stackedBarChart())
        button2.grid(row=2, column=2, padx=10, pady=10)

        button3 = ttk.Button(self, text="Pie Chart", command=lambda: charts.pieChart())
        button3.grid(row=3, column=2, padx=10, pady=10)

        button4 = ttk.Button(self, text="Nested Pie Chart", command=lambda: charts.nestedPieChart())
        button4.grid(row=4, column=2, padx=10, pady=10)


app = App()
app.mainloop()
