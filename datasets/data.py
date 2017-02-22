import csv, json

with open("data.tsv", "rU") as tsvfile:
	tsv = csv.reader(tsvfile, delimiter='\t')
	i = 0
	data = []
	dataset = []
	'''Year (2), Income (7), Region (10), Age (19), Education (23), Jazz(33), Salsa (35), 
		Classical (37), Opera (39), Musical (41), Play (43), Ballet (45), Dance (47), Art Museum (49),
		Craft Fair (51), Festival (52), Parks (53)'''
	for row in tsv:
		for j in range(len(row)):
			if row[j] == ' ':
				row[j] = '0'

		data.append([row[2], row[7], row[10], row[19], row[23], row[33], row[35], row[37], 
			row[39], row[41], row[43], row[45], row[47], row[49], row[51], row[52], row[53]])

artforms = ["Jazz", "Salsa", "Classical", "Opera", "Musical", "Play", "Ballet", 
				"Dance", "Art Museum", "Craft Fair", "Festival", "Parks"]


art_engagement = {"name": "Engagement in Arts", "children": []}

headers = ["Artform", "Year", "Income", "Age", "Education"]

artform_count = {}
for row in artforms:
	artform_count[row] = 0
income = "0 - 15K"
age = 18
educ = "Middle School"
for row in data:
	if row[3] != "AGE":
		age = int(row[3])
	for j in range(len(row[5:])):
		if row[j+5] == "1":
			artform_count[artforms[j]] += 1
			if row[1] == "1" or row[1] == "2" or row[1] == "3" or row[1] == "4" or row[1] == "5" or row[1] == "21" or row[1] == "22" or row[1] == "23" or row[1] == "24" or row[1] == "25" or row[1] == "26" or row[1] == "27" or row[1] == "40":
				income = "0 - 15K"
			if row[1] == "6" or row[1] == "7" or row[1] == "8" or row[1] == "19" or row[1] == "28":
				income = "15K - 30K"
			if row[1] == "9" or row[1] == "10" or row[1] == "11" or row[1] == "30" or row[1] == "41":
				income = "30K - 50K"
			if row[1] == "12" or row[1] == "13" or row[1] == "14" or row[1] == "17":
				income = "50K - 75K"
			if row[1] == "15" or row[1] == "16" or row[1] == "18" or row[1] == "19":
				income = "75K+"
			if row[4] == "1":
				educ = "Middle School"
			if row[4] == "2":
				educ = "High School"
			if row[4] == "3":
				educ = "High School Graduate"
			if row[4] == "4":
				educ = "College"
			if row[4] == "5":
				educ = "College Graduate"
			if row[4] == "6":
				educ = "Post Graduate Degree"
			dataset.append([artforms[j], row[0], income, age, educ])

for entry in artform_count:
	art_engagement["children"].append({"name": entry, "size": artform_count[entry]})

with open("treemap.json", "w") as fjson:
	json.dump(art_engagement, fjson)

for row in dataset:
	if row[3] >= 18 and row[3] <= 24:
		row[3] = "18 - 24"
	if row[3] >= 25 and row[3] <= 34:
		row[3] = "25 - 34"
	if row[3] >= 35 and row[3] <= 44:
		row[3] = "35 - 44"
	if row[3] >= 45 and row[3] <= 54:
		row[3] = "45 - 54"
	if row[3] >= 55 and row[3] <= 64:
		row[3] = "55 - 64"
	if row[3] >= 65 and row[3] <= 74:
		row[3] = "65 - 74"
	if row[3] >= 75 and row[3] < 200:
		row[3] = "75+"
	print row[3]

with open("parsets.csv", "w") as csvfile:
	csv = csv.writer(csvfile)
	csv.writerow(headers)
	csv.writerows(dataset)


