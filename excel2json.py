import pandas as pd
import time
import jsonschema
import schema
import math
import random
# Convert the dictionary pandas format to array with objects
def pandasDictFormat(ditionary):
    data = []
    int2string = ['phone','contactPhone','IDNumber','numChildren','altContactPhone']
                  
    for counter in range(len(ditionary['roomNum'])):
        dict1 = {}
        for key, val in ditionary.items():

            if key in int2string and val[counter] != None:
                dict1[key] = str(val[counter])
            else:
                dict1[key] = val[counter]
        data.append(dict1)
    return data



def noneCheck(num):
    try:
        if math.isnan(num):
            return None
        else:
            return num
    except:
        return num





# Validate the date and time format and replacing it to timestamp
def shaiValidate(data):
    
    dateKeys = ['releaseDate',
            'hafnayaTime',
            'arrivingTime',
            'collectingDate',
            'receptionTime', 'birthDate']


    for key, val in data.items():

        if key in dateKeys and val != '' and val != None:
            #print(type(val))
            val = str(val)
            print(type(val))
            try:
                data[key] = time.mktime(time.strptime(str(val), "%d.%m.%Y %H:%M:%S")) * 1000

            
                try:
                    data[key] = time.mktime(time.strptime(str(val), "%d.%m.%Y")) * 1000
                except:
                    data[key] = None

            except:
                    data[key] = None

            

    return data



def formatExcel(path):
    a = pd.read_excel(path)

    for column in a.columns:
        a[column] = a[column].apply(noneCheck)

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

    filename = str(random.random()).replace('.','')

    path = filename +'.xlsx'

    data.to_excel(path)

    return path

