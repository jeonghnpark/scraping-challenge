import csv
name="filename/good"
print(name)
name=name.replace('/','')
print(name)
file_name = name + '.csv'
file = open(file_name, mode="w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(['title', 'location', 'work_time', 'payment', 'regDate'])
