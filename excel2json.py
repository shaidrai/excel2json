import pandas as pd
import time
import jsonschema
import schema


# Convert the dictionary pandas format to array with objects
def pandasDictFormat(ditionary):
    data = []
    int2string = ['phone','contactPhone','IDNumber','numChildren','altContactPhone']
                  
    for counter in range(len(ditionary['roomNum'])):
        dict1 = {}
        for key, val in ditionary.items():
            if key in int2string:
                dict1[key] = str(val[counter])
            else:
                dict1[key] = val[counter]
        data.append(dict1)
    return data


# Validate the date and time format and replacing it to timestamp
def shaiValidate(data):
    
    dateKeys = ['releaseDate',
            'hafnayaTime',
            'arrivingTime',
            'collectingDate',
            'receptionTime']


    for key, val in data.items():




        if key in dateKeys and val != '' and str(type(val)) == "<class 'str'>":

            print('shaishai')
 

            data[key] = time.mktime(time.strptime(val, "%d.%m.%Y %H:%M")) * 1000

        elif key == 'birthDate' and val != '' and str(type(val)) == "<class 'str'>":


            data[key] = time.mktime(time.strptime(val, "%d.%m.%Y")) * 1000

    return data


def formatExcel(path):
    a = pd.read_excel(path)


    data = pandasDictFormat(a.to_dict())



    for row in data:

        # jsonschema.validate(row, schema=schema.schema)
        shaiValidate(row)
        # Use try except outside of the function
    return data


def formatJson(data):

    d = {}
    
    for key in schema.schema['properties'].keys():
        for obj in data:
            try:
                
                value = obj[key]
                
            except:
                value = None
                
            try:
                d[key].append(value)
            except:
                d[key] = []
                d[key].append(value)
                   

 
    data = pd.DataFrame(d)

    data.to_excel('excel.xlsx')

    return 'excel.xlsx'

