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


def getByCareer(query, career):
    cursor.execute(query, career)
    res = []

    for n in cursor:
        res.append(n)

    lenRes.append(len(res))


def getByYear(query, y, career):
    cursor.execute(query, (y, career))
    res = []

    for n in cursor:
        res.append(n)

    lenYearRes.append(len(res))


fullCareerArr = [["Ing. Civil", "%Civil%"],  # 0
                 ["Diplomacia y Relaciones Internacionales", "%Diplomacia%"],  # 1
                 ["Comunicación y Relaciones Públicas", "%Comunicaci%"],  # 2
                 ["Medicina y Cirugía", "%Medicina%"],  # 3
                 ["Arquitectura", "%Arquitect%"],  # 4
                 ["Diseño y Comunicación Visual", "%Dise%"],  # 5
                 ["Marketing y Publicidad", "%Marketing%"],  # 6
                 ["Ingeniería Industrial", "%Industrial%"],  # 7
                 ["Contabilidad y Finanzas", "%Contabilidad%"],  # 8
                 ["Negocios Internacionales", "%Negocios%"],  # 9
                 ["Administración de Empresas", "%Administraci%"],  # 10
                 ["Gerencia Informática", "%Gerencia%"],  # 11
                 ["Economía Empresarial", "%Econom%"],  # 12
                 ["Cirujano Dentista", "%Dentista%"],  # 13
                 ["Science in International Development with Concentration in Tourism Development", "%International%"],
                 # 14
                 ["Derecho", "%Derecho%"],  # 15
                 ["Ing. en Sistemas de Información", "%Sistemas%"],  # 16
                 ["Science in Global Management", "%Management%"]]  # 17

careerArr = [fullCareerArr[3], fullCareerArr[7], fullCareerArr[10], fullCareerArr[15]]

for e in careerArr:
    legendArr.append(e[0])

    q = '''SELECT * FROM uber_grad WHERE "Titulo_y_grado_otorgado" LIKE %s;'''
    getByCareer(q, (e[1],))

    yearQ = '''SELECT * FROM uber_grad WHERE "Graduacion" > %s AND "Titulo_y_grado_otorgado" LIKE %s'''
    getByYear(yearQ, year, (e[1],))

for i in range(len(lenRes)):
    yearDiffRes.append(lenRes[i] - lenYearRes[i])

'''
lim = SELECT * FROM uber_grad WHERE "Graduacion" > 2022;
cursor.execute(lim)
resLim = []

for elem in cursor:
    resLim.append(elem)
'''
