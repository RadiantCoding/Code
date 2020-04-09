import openpyxl
from pathlib import Path
xlsxFile = Path('','Customers.xlsx')
workbook = openpyxl.load_workbook(xlsxFile)
sheet = workbook.active

data = {}

for i, row in enumerate(sheet.iter_rows(values_only=True)):
	if i == 0:
		data[row[0]] = []
		data[row[1]] = []
		data[row[2]] = []
		data[row[3]] = []
		data[row[4]] = []
	else:
		data['id'].append(row[0])
		data['company'].append(row[1])
		data['last_name'].append(row[2])
		data['first_name'].append(row[3])
		data['job_title'].append(row[4])
		
print(data)



