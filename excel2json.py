import pandas as pd
import time
import jsonschema
import schema
# Convert the dictionary pandas format to array with objects
def pandasDictFormat(ditionary):
    data = []
    for counter in range(len(ditionary['room'])):
        dict1 = {}
        for key, val in ditionary.items():
            if key == 'phone' or key == 'replacedPhone' or key == 'IDNumber':
                dict1[key] = str(val[counter])
            else:
                dict1[key] = val[counter]
        data.append(dict1)
    return data


# Validate the date and time format and replacing it to timestamp
def shaiValidate(data):
    dateKeys = ['hafnayaDate', 'hafnayaTime', 'receptionDate', 'receptionTime', 'receptionTime', 'collectingDate', 'arrivingTime', 'releaseDate']
    for key, val in data.items():
        if key in dateKeys:
            data[key] = time.mktime(time.strptime(val, "%d.%m.%Y %H:%M")) * 1000
    return data


def formatExcel(path):
    a = pd.read_excel(path)
    data = pandasDictFormat(a.to_dict())

    for row in data:
        jsonschema.validate(row, schema=schema.schema)
        shaiValidate(row)
        # Use try except outside of the function
    return data

