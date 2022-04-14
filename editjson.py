import json
exchanges = {
    "NSE":"nseequitylist.json",
    "BSE":"bseequitylist.json"
}
inpt = []
for key in exchanges:
    file = open(exchanges[key])
    data = json.load(file)
    for element in data:
        details = {}
        if(element['SERIES'] == 'EQ'):
            details['SYMBOL'] = element['SYMBOL']
            details['NAME OF COMPANY'] = element['NAME OF COMPANY']
            details['SERIES'] = element['SERIES']
            details['ISIN NUMBER'] = element['ISIN NUMBER']            
            details['EXCHANGE'] = key
            inpt.append(details)
    file.close()
with open("data.json", "w") as outfile:
    json.dump(inpt, outfile, indent=2)