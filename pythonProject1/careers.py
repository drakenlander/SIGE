import psycopg2 as psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin")

cursor = conn.cursor()
legendArr = []
lenRes = []
year = 2021
lenYearRes = []
yearDiffRes = []
fullCareerArr = [["Ing. Civil", "%Civil%"],  # 0
                 ["Diplomacia y Rel. Internacionales", "%Diplomacia%"],  # 1
                 ["Comunicación y Rel. Públicas", "%Comunicaci%"],  # 2
                 ["Medicina y Cirugía", "%Medicina%"],  # 3
                 ["Arquitectura", "%Arquitect%"],  # 4
                 ["Diseño y Comunicación Visual", "%Dise%"],  # 5
                 ["Marketing y Publicidad", "%Marketing%"],  # 6
                 ["Ing. Industrial", "%Industrial%"],  # 7
                 ["Contabilidad y Finanzas", "%Contabilidad%"],  # 8
                 ["Negocios Internacionales", "%Negocios%"],  # 9
                 ["Administración de Empresas", "%Administraci%"],  # 10
                 ["Gerencia Informática", "%Gerencia%"],  # 11
                 ["Economía Empresarial", "%Econom%"],  # 12
                 ["Cirujano Dentista", "%Dentista%"],  # 13
                 ["Science in International Development", "%International%"],
                 # 14
                 ["Derecho", "%Derecho%"],  # 15
                 ["Ing. en Sistemas", "%Sistemas%"],  # 16
                 ["Science in Global Management", "%Management%"]]  # 17
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


def select(e):
    legendArr.append(e[0])

    q = '''SELECT * FROM uber_grad WHERE "Titulo_y_grado_otorgado" LIKE %s;'''
    getByCareer(q, (e[1],))

    yearQ = '''SELECT * FROM uber_grad WHERE "Graduacion" > %s AND "Titulo_y_grado_otorgado" LIKE %s'''
    getByYear(yearQ, year, (e[1],))

    # for k in range(len(lenRes)):
    # yearDiffRes.append(lenRes[k] - lenYearRes[k])


def addCareer(career):
    for i in range(len(fullCareerArr)):
        if fullCareerArr[i][0] == career:
            careerArr.append(fullCareerArr[i])
            select(careerArr[-1])


def removeCareer(career):
    for i in careerArr:
        if i[0] == career:
            index = careerArr.index(i)

            careerArr.remove(i)
            legendArr.remove(legendArr[index])
            lenRes.remove(lenRes[index])
            lenYearRes.remove(lenYearRes[index])
            yearDiffRes.remove(yearDiffRes[index])


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
