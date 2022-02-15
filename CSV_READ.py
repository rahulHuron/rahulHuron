import csv

with open('EmailTemplate.csv') as csvfile:
    csvReader=csv.reader(csvfile)
    id = []
    date = []
    for row in csvReader:
        id.append(row[0])
        date.append(row[1])
print(id)
print(date)

Index = id.index('0050B000007vgOSQAY')
loanStatusIndex = date[Index]
print(loanStatusIndex)

with open('loanapp.csv','a') as Wfile:
    write = csv.writer(Wfile)
    write.writerow(["Rahul","Cleared"])



