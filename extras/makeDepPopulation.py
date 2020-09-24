from openpyxl import load_workbook

filename = 'poblacion_dpto.csv'

csvFN = open(filename, 'w')
wb = load_workbook('poblacion_dpto.xlsx')
ws = wb['Sheet1']

csvFN.write('in1,nombre,pob_total\n')

for row in ws.values:
    try:
        if 'AREA' in row[0]:
            indecCode = row[0][7:]
            name = row[1]
            newAreaFound = True
        if ' Total' == row[0] and newAreaFound:
            totPopulation = int(row[3])
            print(indecCode, name, totPopulation)
            csvFN.write(f'{indecCode:5},{name},{totPopulation}\n')
            newAreaFound = False
    except:
        pass


csvFN.close()
