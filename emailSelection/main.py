import psycopg2 as psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin")

cursor = conn.cursor()

selectDistinctCareers = '''SELECT DISTINCT "PROGRAMA" FROM public.excelforconversion WHERE "PROGRAMA" IS NOT NULL;'''
cursor.execute(selectDistinctCareers)

careerArr = []
emailArr = []

for i in cursor:
    careerArr.append(i)

emailDict = {key: [] for key in careerArr}

for i in careerArr:
    formattedIter = "'" + i[0] + "'"

    selectEmails = '''SELECT "EMAIL", "EMAIL_PERSONAL" FROM public.excelforconversion WHERE "PROGRAMA" = {0} AND 
    "EMAIL" != '.' AND "EMAIL" != 'nd';'''.format(formattedIter)
    cursor.execute(selectEmails)

    for j in cursor:
        emailArr.append(j)

    emailDict[i] += emailArr
    emailArr.clear()

# print(len(emailDict))
# print(emailDict)

selectPhoneNumbers = '''SELECT "CELULAR", "TELEFONO_1", "TELEFONO_2"
                        FROM public.excelforconversion
                        WHERE "PROGRAMA" = 'LICENCIATURA EN INGENIERIA INDUSTRIAL'
                        OR "PROGRAMA" = 'LICENCIATURA EN ADMINISTRACION DE EMPRESAS';'''
cursor.execute(selectPhoneNumbers)

phoneNumberArr = []

for i in cursor:
    if not ((i[0] is None or i[0] == 0) and (i[1] is None or i[1] == 0) and (i[2] is None or i[2] == 0)):
        phoneNumberArr.append(i)

formattedArr = [[0] * 3] * len(phoneNumberArr)
file = open("phnum.csv", "w")

for i in range(len(formattedArr)):
    for j in range(3):
        elem = phoneNumberArr[i][j]

        if elem is None:
            elem = 0

        if elem != 0:
            jStr = str(elem)

            if len(jStr) < 7:
                elem = 0

            if len(jStr) == 7:
                jStr = "8" + jStr
                elem = int(jStr)

        formattedArr[i][j] = elem

        if str(formattedArr[i][j])[0] == "2":
            formattedArr[i][j] = 0

    if not (formattedArr[i][0] + formattedArr[i][1] + formattedArr[i][2] == 0):
        iStr = str(formattedArr[i])[1:-1]

        file.write(iStr + "\n")

file.close()
