import tkinter as tk
from tkinter import ttk
import matplotlib
import careers
import charts

matplotlib.use('TkAgg')

font = ("Verdana", 28)

toggles = [True] * len(careers.fullCareerArr)


# TODO: Add Year filter; Add styling to toggle buttons
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        title_frame = tk.Frame(self, background="white")
        title_frame.pack(side="top", pady=50)
        a_careers_frame = tk.Frame(self, background="white")
        a_careers_frame.pack(side='left', padx=50)
        b_careers_frame = tk.Frame(self, background="white")
        b_careers_frame.pack(side='left')
        charts_frame = tk.Frame(self, background="white")
        charts_frame.pack(side='right', padx=100)

        def buttonToggle(toggle, n, career):
            if toggle[n]:
                careers.addCareer(career)
                toggle[n] = False
            else:
                careers.removeCareer(career)
                toggle[n] = True

        title = tk.Label(title_frame, background='white', text="Sistema de Información de Graduados y Egresados",
                         font=font)
        title.bind('<Configure>', lambda e: title.config(wraplength=self.winfo_width()))
        title.pack(side="top", fill="x", expand=True)

        tk.Checkbutton(a_careers_frame, text="Administración de Empresas", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 0, "Administración de Empresas")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Arquitectura", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 1, "Arquitectura")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Cirujano Dentista", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 2, "Cirujano Dentista")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Comunicación y Rel. Públicas", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 3,
                                                    "Comunicación y Rel. Públicas")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Contabilidad y Finanzas", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 4, "Contabilidad y Finanzas")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Derecho", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 5, "Derecho")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Diplomacia y Rel. Internacionales", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 6,
                                                    "Diplomacia y Rel. Internacionales")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Diseño y Comunicación Visual", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 7, "Diseño y Comunicación Visual")).pack(fill="x", pady=5)

        tk.Checkbutton(a_careers_frame, text="Economía Empresarial", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 8, "Economía Empresarial")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Gerencia Informática", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 9, "Gerencia Informática")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Ingeniería Civil", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 10, "Ing. Civil")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Ingeniería en Sistemas de Información", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 11,
                                                    "Ing. en Sistemas")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Ingeniería Industrial", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 12, "Ing. Industrial")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Marketing y Publicidad", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 13, "Marketing y Publicidad")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Medicina y Cirugía", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 14, "Medicina y Cirugía")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Negocios Internacionales", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 15, "Negocios Internacionales")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Science in Global Management", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 16, "Science in Global Management")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame,
                       text="Science in International Development",
                       background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 17,
                                                    "Science in International Development")).pack(fill="x", pady=5)

        ttk.Button(charts_frame, text="Bar Chart",
                   command=lambda: charts.barChart()).pack(fill="x", pady=5)

        ttk.Button(charts_frame, text="Stacked Bar Chart", command=lambda: charts.stackedBarChart()).pack(fill="x",
                                                                                                          pady=5)

        ttk.Button(charts_frame, text="Pie Chart", command=lambda: charts.pieChart()).pack(fill="x", pady=5)

        ttk.Button(charts_frame, text="Nested Pie Chart", command=lambda: charts.nestedPieChart()).pack(fill="x",
                                                                                                        pady=5)


app = App()

app.title("Sistema de Información de Graduados y Egresados")
app.configure(background='white')
app.geometry("%dx%d" % (900, 720))

app.mainloop()
