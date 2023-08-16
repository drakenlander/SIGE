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

selectPhoneNumbers = '''SELECT "NOMBRE_ESTUDIANTE", "CIF", "CELULAR", "TELEFONO_1", "TELEFONO_2"
                        FROM public.excelforconversion
                        WHERE "PROGRAMA" = 'LICENCIATURA EN INGENIERIA INDUSTRIAL'
                        OR "PROGRAMA" = 'LICENCIATURA EN ADMINISTRACION DE EMPRESAS';'''
cursor.execute(selectPhoneNumbers)

phoneNumberArr = []

for i in cursor:
    if not ((i[2] is None or i[2] == 0) and (i[3] is None or i[3] == 0) and (i[4] is None or i[4] == 0)):
        phoneNumberArr.append(i)

formattedArr = [[0] * 5] * len(phoneNumberArr)
file = open("phnum.csv", "w")

for i in range(len(formattedArr)):
    for j in range(5):
        elem = phoneNumberArr[i][j]

        if j != 0 and j != 1:
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

        else:
            formattedArr[i][j] = elem

    if not (formattedArr[i][2] + formattedArr[i][3] + formattedArr[i][4] == 0):
        iStr = str(formattedArr[i])[1:-1]

        file.write(iStr + "\n")

file.close()
