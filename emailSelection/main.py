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

print(len(emailDict))
print(emailDict)
