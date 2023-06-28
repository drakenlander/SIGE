import psycopg2 as psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin")

cursor = conn.cursor()
legendArr = []
lenRes = []
yearStorage = []
lenYearRes = []
yearDiffRes = []
fullCareerArr = [["Administración de Empresas", "%Administraci%"],  # 0
                 ["Arquitectura", "%Arquitect%"],  # 1
                 ["Cirujano Dentista", "%Dentista%"],  # 2
                 ["Comunicación y Rel. Públicas", "%Públicas%"],  # 3
                 ["Contabilidad y Finanzas", "%Contabilidad%"],  # 4
                 ["Derecho", "%Derecho%"],  # 5
                 ["Diplomacia y Rel. Internacionales", "%Diplomacia%"],  # 6
                 ["Diseño y Comunicación Visual", "%Dise%"],  # 7
                 ["Economía Empresarial", "%Econom%"],  # 8
                 ["Gerencia Informática", "%Gerencia%"],  # 9
                 ["Ing. Civil", "%Civil%"],  # 10
                 ["Ing. en Sistemas", "%Sistemas%"],  # 11
                 ["Ing. Industrial", "%Industrial%"],  # 12
                 ["Marketing y Publicidad", "%Marketing%"],  # 13
                 ["Medicina y Cirugía", "%Medicina%"],  # 14
                 ["Negocios Internacionales", "%Negocios%"],  # 15
                 ["Global Management", "%Global%"],  # 16
                 ["International Development", "%International%"]]  # 17
# careerArr = [fullCareerArr[3], fullCareerArr[7], fullCareerArr[10], fullCareerArr[15]]
careerArr = []
fullColumnArr = ["uber_id",  # 0
                 "id",  # 1
                 "nombre_graduado",  # 2
                 "documento_de_identidad",  # 3
                 "graduacion",  # 4
                 "titulo_y_grado_otorgado",  # 5
                 "institucion_emisora",  # 6
                 "tomo",  # 7
                 "folio_y_numero",  # 8
                 "fecha_de_emision_del_titulo",  # 9
                 "plan_de_estudios"]  # 10
columnArr = ["0"] * len(fullColumnArr)
columnArr[0] = 'uber_id'
tableArr = []
selection = []


def selectConversion(q):
    cursor.execute(q)
    conn.commit()


def getAllTables():
    tableArr.clear()

    cursor.execute('''SELECT * FROM information_schema.tables WHERE table_schema = 'public';''')

    for table in cursor:
        tableArr.append(table[2])

    return tableArr


def tabulate(carArr, colArr):
    columnList = ', '.join(str(i) for i in colArr)

    r_set = []

    for i in range(len(carArr)):
        formattedCar = "'" + carArr[i][1] + "'"
        q = '''SELECT {0} FROM {1} WHERE "titulo_y_grado_otorgado" LIKE {2};'''.format(columnList, selection[-1],
                                                                                       formattedCar)
        cursor.execute(q)

        for r in cursor:
            r_set.append(r)

    return r_set


def getByCareer(query):
    cursor.execute(query)
    res = []

    for n in cursor:
        res.append(n)

    lenRes.append(len(res))


def getByYear(query, career):
    cursor.execute(query)
    res = []
    pRes = []

    for n in cursor:
        res.append(n)

    neuQ = '''SELECT * FROM {0} WHERE "titulo_y_grado_otorgado" LIKE {1};'''.format(selection[-1], career)

    cursor.execute(neuQ)

    for m in cursor:
        pRes.append(m)

    lenYearRes.append(len(res))
    yearDiffRes.append(len(pRes) - len(res))


def select(e, y):
    legendArr.append(e[0])

    neuCareer = "'" + e[1] + "'"

    q = '''SELECT * FROM {0} WHERE "titulo_y_grado_otorgado" LIKE {1};'''.format(selection[-1], neuCareer)
    getByCareer(q)

    yearQ = '''SELECT * FROM {0} WHERE "graduacion" > {1} AND "titulo_y_grado_otorgado" LIKE {2};'''.format(selection[-1], y, neuCareer)
    getByYear(yearQ, neuCareer)

    # for k in range(len(lenRes)):
    # yearDiffRes.append(lenRes[k] - lenYearRes[k])


def addCareer(career, y):
    for i in range(len(fullCareerArr)):
        if fullCareerArr[i][0] == career:
            yearStorage.append(y)

            careerArr.append(fullCareerArr[i])
            select(careerArr[-1], y)


def removeCareer(career):
    for i in careerArr:
        if i[0] == career:
            index = careerArr.index(i)

            careerArr.remove(i)
            legendArr.remove(legendArr[index])
            lenRes.remove(lenRes[index])
            lenYearRes.remove(lenYearRes[index])
            yearDiffRes.remove(yearDiffRes[index])


def clearArr():
    careerArr.clear()
    legendArr.clear()
    lenRes.clear()
    lenYearRes.clear()
    yearDiffRes.clear()


def getLength():
    length = len(lenRes)

    return length


def addColumn(column):
    for i in range(len(fullColumnArr)):
        if fullColumnArr[i] == column:
            # columnArr.append(fullColumnArr[i])
            columnArr[i] = fullColumnArr[i]


def removeColumn(column):
    for i in range(len(columnArr)):
        if columnArr[i] == column:
            columnArr[i] = "0"

    columnArr[0] = 'uber_id'


def clearColumnArr():
    for i in range(len(columnArr)):
        columnArr[i] = "0"

    columnArr[0] = 'uber_id'


'''
lim = SELECT * FROM uber_grad WHERE "Graduacion" > 2022;
cursor.execute(lim)
resLim = []

for elem in cursor:
    resLim.append(elem)
'''
