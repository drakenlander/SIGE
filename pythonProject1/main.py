import tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog
from datetime import datetime
import matplotlib
import careers
import charts

# TODO: Add Excel file visualization with filtering
# TODO: Add Excel file row selection
# TODO: Add Excel charting algorithms
# TODO: Add Excel file conversion (?)
# TODO: Add table Year Filter

matplotlib.use('TkAgg')

toggles = [True] * len(careers.fullCareerArr)
col_toggles = [True] * 11
years = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
exFile = [""]
lastFrameRemembrance = []


def uploadAction(exTrv):
    filename = filedialog.askopenfilename()
    exFile.append(filename)

    for row in exTrv.get_children():
        exTrv.delete(row)

    df = pd.read_excel(exFile[-1])
    headers = list(df)

    exTrv['columns'] = headers
    exTrv['show'] = 'headings'

    r_set = df.to_numpy().tolist()

    for i in headers:
        exTrv.column(i, width=100, anchor='c')
        exTrv.heading(i, text=str(i))

    for dt in r_set:
        v = [r for r in dt]
        exTrv.insert("", 'end', iid=v[0], values=v)

    return df


def passFileName(f, v):
    if exFile[-1] != "":
        f.append(exFile[-1])
        v.set(f[-1])


def tableView(trv):
    display = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    r_set = careers.tabulate(careers.careerArr, careers.columnArr)

    for r in trv.get_children():
        trv.delete(r)

    for dt in r_set:
        trv.insert("", "end", iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6],
                                                             dt[7], dt[8], dt[9], dt[10]))

    for col in range(len(r_set[0])):
        if r_set[0][col] == 0 or r_set[0][col] == "0":
            display[col] = 999

    display = [i for i in display if i != 999]

    trv.config(displaycolumns=display)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Table, Columns, ExcelCharts, ExcelTable):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(StartPage)

        trv = ttk.Treeview(self.frames[Table])
        trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
        trv['show'] = 'headings'
        horScrollBar = ttk.Scrollbar(self.frames[Table], orient="horizontal", command=trv.xview)
        verScrollBar = ttk.Scrollbar(self.frames[Table], orient="vertical", command=trv.yview)
        horScrollBar.pack(side="bottom", fill="x")
        verScrollBar.pack(side="right", fill="y")
        trv.configure(xscrollcommand=horScrollBar.set, yscrollcommand=verScrollBar.set)
        trv.pack(side="left", fill="both")

        exTrv = ttk.Treeview(self.frames[ExcelTable])
        exHorScrollBar = ttk.Scrollbar(self.frames[ExcelTable], orient="horizontal", command=exTrv.xview)
        exVerScrollBar = ttk.Scrollbar(self.frames[ExcelTable], orient="vertical", command=exTrv.yview)
        exHorScrollBar.pack(side="bottom", fill="x")
        exVerScrollBar.pack(side="right", fill="y")
        exTrv.configure(xscrollcommand=exHorScrollBar.set, yscrollcommand=exVerScrollBar.set)
        exTrv.pack(side="left", fill="both")

        def checkTableView():
            if lastFrameRemembrance[-1] != "<class '__main__.Table'>":
                tableView(trv)

                self.showFrame(Table)

        def writeFile(selectAll):
            now = datetime.now()
            dt_string = now.strftime("%d%m%Y_%H%M%S")

            if selectAll:
                for i in trv.get_children():
                    trv.selection_add(i)

                sel = select()
                copySelection(sel)

                file = open(dt_string + ".csv", "w", encoding="utf-8")
                file.write(sel)

            else:
                sel = select()

                if sel != "":
                    file = open(dt_string + ".csv", "w", encoding="utf-8")
                    file.write(sel)

        def select():
            curItems = trv.selection()
            copy = ""

            for i in curItems:
                row = trv.item(i).get("values")

                for j in row:
                    if j != 0:
                        copy = copy + str(j) + ", "

                copy = copy[:-2] + "\n"

            copy = copy[:-1]

            return copy

        def copySelection(selection):
            self.clipboard_clear()
            self.clipboard_append(selection)

        trv.column("1", width=50, anchor='c')
        trv.column("2", width=50, anchor='c')
        trv.column("3", width=225, anchor='w')
        trv.column("4", width=175, anchor='w')
        trv.column("5", width=100, anchor='c')
        trv.column("6", width=325, anchor='w')
        trv.column("7", width=175, anchor='w')
        trv.column("8", width=75, anchor='c')
        trv.column("9", width=100, anchor='c')
        trv.column("10", width=175, anchor='c')
        trv.column("11", width=200, anchor='w')
        trv.heading("1", text="#")
        trv.heading("2", text="ID")
        trv.heading("3", text="Nombre del Graduado")
        trv.heading("4", text="Documento de Identidad")
        trv.heading("5", text="Graduación")
        trv.heading("6", text="Título y Grado Otorgado")
        trv.heading("7", text="Institución Emisora")
        trv.heading("8", text="Tomo")
        trv.heading("9", text="Folio y Número")
        trv.heading("10", text="Fecha de Emisión del Título")
        trv.heading("11", text="Plan de Estudios")

        trv.bind('<ButtonRelease-1>', lambda e: copySelection(select()))

        menubar = tk.Menu(self)
        pg_menu = tk.Menu(menubar, tearoff=False)
        tableMenu = tk.Menu(pg_menu, tearoff=False)
        csvMenu = tk.Menu(tableMenu, tearoff=False)
        ex_menu = tk.Menu(menubar, tearoff=False)

        menubar.add_cascade(
            label="PostgreSQL",
            menu=pg_menu,
            underline=0
        )
        menubar.add_cascade(
            label="Microsoft Excel",
            menu=ex_menu,
            underline=0
        )

        pg_menu.add_command(label="Chart from DB", command=lambda: self.showFrame(StartPage))
        pg_menu.add_cascade(
            label="Table View",
            menu=tableMenu
        )
        tableMenu.add_command(label="Visualize DB", command=lambda: [tableView(trv), self.showFrame(Table)])
        tableMenu.add_command(label="Filter by column", command=lambda: self.showFrame(Columns))
        tableMenu.add_cascade(
            label="Generate .csv",
            menu=csvMenu
        )
        csvMenu.add_command(label="All rows", command=lambda: [tableView(trv), self.showFrame(Table), writeFile(True)])
        csvMenu.add_command(label="Selected rows only", command=lambda: [checkTableView(), writeFile(False)])

        ex_menu.add_command(label="Chart from spreadsheet", command=lambda: self.showFrame(ExcelCharts))
        ex_menu.add_command(label="Visualize spreadsheet", command=lambda: self.showFrame(ExcelTable))
        ex_menu.add_command(label="Upload spreadsheet", command=lambda: uploadAction(exTrv))

        self.configure(menu=menubar, background="white")

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        lastFrameRemembrance.append(str(cont))


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")
        self.controller = controller

        a_careers_frame = tk.Frame(self, background="white")
        a_careers_frame.pack(side="left", padx=50)
        b_careers_frame = tk.Frame(self, background="white")
        b_careers_frame.pack(side="left")
        charts_frame = tk.Frame(self, background="white")
        charts_frame.pack(side="right", padx=100)

        def getYear():
            selection = yearFilter.get()

            return selection

        def buttonToggle(toggle, n, career):
            if toggle[n]:
                careers.addCareer(career, getYear())
                toggle[n] = False
            else:
                careers.removeCareer(career)
                toggle[n] = True

        def reset(a_parent_widget, b_parent_widget):
            a_children_widgets = a_parent_widget.winfo_children()
            b_children_widgets = b_parent_widget.winfo_children()

            for i in range(len(a_children_widgets)):
                if isinstance(a_children_widgets[i], tk.Checkbutton):
                    a_children_widgets[i].deselect()

            for j in range(len(b_children_widgets)):
                if isinstance(b_children_widgets[j], tk.Checkbutton):
                    b_children_widgets[j].deselect()

            for k in range(len(toggles)):
                toggles[k] = True

            careers.clearArr()

        tk.Label(a_careers_frame, text="Year Filter:", background="white").pack()
        yearFilter = ttk.Combobox(b_careers_frame, state="readonly", values=years)
        yearFilter.bind("<<ComboboxSelected>>", getYear())
        yearFilter.pack(fill="x")
        yearFilter.current(0)

        tk.Label(a_careers_frame, background="white").pack()
        tk.Label(b_careers_frame, background="white").pack()

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

        tk.Checkbutton(b_careers_frame, text="Ing. Civil", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 10, "Ing. Civil")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Ing. en Sistemas", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 11,
                                                    "Ing. en Sistemas")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Ing. Industrial", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 12, "Ing. Industrial")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Marketing y Publicidad", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 13, "Marketing y Publicidad")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Medicina y Cirugía", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 14, "Medicina y Cirugía")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Negocios Internacionales", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 15, "Negocios Internacionales")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame, text="Global Management", background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 16, "Global Management")).pack(fill="x", pady=5)

        tk.Checkbutton(b_careers_frame,
                       text="International Development",
                       background="white", anchor="w",
                       command=lambda: buttonToggle(toggles, 17,
                                                    "International Development")).pack(fill="x", pady=5)

        tk.Button(a_careers_frame, text="Reset array...", background="white", anchor="w",
                  command=lambda: reset(a_careers_frame, b_careers_frame)).pack(fill="x", pady=5)

        tk.Label(b_careers_frame, background="white", anchor="w").pack(fill="x", pady=5)

        ttk.Button(charts_frame, text="Bar Chart",
                   command=lambda: charts.barChart()).pack(fill="x", pady=5)

        ttk.Button(charts_frame, text="Stacked Bar Chart", command=lambda: charts.stackedBarChart()).pack(fill="x",
                                                                                                          pady=5)

        ttk.Button(charts_frame, text="Dispersion Chart", command=lambda: charts.dispersionChart()).pack(fill="x",
                                                                                                         pady=5)

        ttk.Button(charts_frame, text="Pie Chart", command=lambda: charts.pieChart()).pack(fill="x", pady=5)

        ttk.Button(charts_frame, text="Nested Pie Chart", command=lambda: charts.nestedPieChart()).pack(fill="x",
                                                                                                        pady=5)


class Table(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")
        self.controller = controller


class Columns(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")
        self.controller = controller

        columns_frame = tk.Frame(self, background="white")
        columns_frame.pack(side="left", padx=50)

        def buttonToggle(col_toggle, n, column):
            if col_toggle[n]:
                careers.addColumn(column)
                col_toggle[n] = False
            else:
                careers.removeColumn(column)
                col_toggle[n] = True

        def reset(col_frame):
            columns_children_widgets = col_frame.winfo_children()

            for i in range(len(columns_children_widgets)):
                if isinstance(columns_children_widgets[i], tk.Checkbutton):
                    columns_children_widgets[i].deselect()

            for k in range(len(col_toggles)):
                col_toggles[k] = True

            careers.clearColumnArr()

        tk.Checkbutton(columns_frame, text="ID", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 1, "id")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Nombre del Graduado", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 2, "nombre_graduado")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Documento de Identidad", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 3, "documento_de_identidad")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Año de Graduación", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 4, "graduacion")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Título y Grado Otorgado", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 5, "titulo_y_grado_otorgado")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Institución Emisora", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 6, "institucion_emisora")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Tomo", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 7, "tomo")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Folio y Número", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 8, "folio_y_numero")).pack(fill="x", pady=5)

        tk.Checkbutton(columns_frame, text="Fecha de Emisión del Título", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 9, "fecha_de_emision_del_titulo")).pack(fill="x",
                                                                                                         pady=5)

        tk.Checkbutton(columns_frame, text="Plan de Estudios", background="white", anchor="w",
                       command=lambda: buttonToggle(col_toggles, 10, "plan_de_estudios")).pack(fill="x", pady=5)

        tk.Button(columns_frame, text="Reset array...", background="white", anchor="w",
                  command=lambda: reset(columns_frame)).pack(fill="x", pady=5)


class ExcelCharts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")
        self.controller = controller

        # file_frame = tk.Frame(self, background="white")
        # file_frame.pack(side="top", padx=50)

        filename = []
        exName = tk.StringVar()
        exName.set("No upload yet...")

        button = ttk.Button(self, text="Refresh", command=lambda: passFileName(filename, exName))
        button.grid(row=0, column=0, padx=5, pady=5)

        label = ttk.Label(self, textvariable=exName, background="white", anchor="center")
        label.grid(row=0, column=1, padx=10, pady=5)


class ExcelTable(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


app = App()

app.title("Sistema de Información de Graduados y Egresados")
app.geometry("%dx%d" % (854, 480))
app.resizable(False, False)

app.mainloop()
