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
                 ["Comunicación y Rel. Públicas", "%Comunicaci%"],  # 3
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


def getByCareer(query, career):
    cursor.execute(query, career)
    res = []

    for n in cursor:
        res.append(n)

    lenRes.append(len(res))


def getByYear(query, y, career):
    cursor.execute(query, (y, career))
    res = []
    pRes = []

    for n in cursor:
        res.append(n)

    cursor.execute('''SELECT * FROM uber_grad WHERE "Titulo_y_grado_otorgado" LIKE %s;''', career)

    for m in cursor:
        pRes.append(m)

    lenYearRes.append(len(res))
    yearDiffRes.append(len(pRes) - len(res))


def select(e, y):
    legendArr.append(e[0])

    q = '''SELECT * FROM uber_grad WHERE "Titulo_y_grado_otorgado" LIKE %s;'''
    getByCareer(q, (e[1],))

    yearQ = '''SELECT * FROM uber_grad WHERE "Graduacion" > %s AND "Titulo_y_grado_otorgado" LIKE %s'''
    getByYear(yearQ, y, (e[1],))

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
            print("removed ", career)
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


'''
lim = SELECT * FROM uber_grad WHERE "Graduacion" > 2022;
cursor.execute(lim)
resLim = []

for elem in cursor:
    resLim.append(elem)
'''
