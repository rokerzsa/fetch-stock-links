import json
file = open('data.json')
data = json.load(file)
max = 0
for element in data:
    length = len(element["NAME OF COMPANY"])
    if length>=64 and length>max:
        max = length
    # print(element["NAME OF COMPANY"])
print(max)
file.close()
