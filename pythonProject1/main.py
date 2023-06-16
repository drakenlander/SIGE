import tkinter as tk
from tkinter import ttk
import matplotlib
import careers
import charts

matplotlib.use('TkAgg')

font = ("Verdana", 35)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        label = ttk.Label(self, background='white', text="Sistema de Información de Graduados y Egresados", font=font)
        label.place(anchor='center', relx=0.5, rely=0.25)

        medicine = ttk.Button(self, text="Medicina y Cirugía", command=lambda: careers.addCareer("Medicina y Cirugía"))
        medicine.place(x=5, y=5)

        marketing = ttk.Button(self, text="Marketing y Publicidad",
                               command=lambda: careers.addCareer("Marketing y Publicidad"))
        marketing.place(x=5, y=50)

        dentistry = ttk.Button(self, text="Cirujano Dentista", command=lambda: careers.addCareer("Cirujano Dentista"))
        dentistry.place(x=5, y=100)

        button1 = ttk.Button(self, text="Bar Chart", command=lambda: charts.barChart())
        button1.place(anchor='center', relx=0.5, rely=0.40)

        button2 = ttk.Button(self, text="Stacked Bar Chart", command=lambda: charts.stackedBarChart())
        button2.place(anchor='center', relx=0.5, rely=0.55)

        button3 = ttk.Button(self, text="Pie Chart", command=lambda: charts.pieChart())
        button3.place(anchor='center', relx=0.5, rely=0.70)

        button4 = ttk.Button(self, text="Nested Pie Chart", command=lambda: charts.nestedPieChart())
        button4.place(anchor='center', relx=0.5, rely=0.85)


app = App()

app.title("Sistema de Información de Graduados y Egresados")
app.configure(background='white')
app.geometry("%dx%d" % (1366, 768))

app.mainloop()
