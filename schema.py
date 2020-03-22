# data format schema
prop = {

'roomNum': {
    'type': 'number',

},
    
    'conversation': {
        'type': 'boolean',

    },
    'religious': {
        'type': 'boolean',

    },
    'phone': {
        'type': 'string',

    },

    'medicalCondition': {
        'type': 'string',

    },

    # Dates

    'releaseDate': {
        'type': 'string',

    },
    'hafnayaTime': {
        'type': 'string',

    },
    'arrivingTime': {
        'type': 'string',

    },
    'collectingDate': {
        'type': 'string',

    },
    'receptionTime': {
        'type': 'string',

    },





'familyStatus': {
    'type': 'string'
},
'numChildren': {
    'type': 'string'
},

'sex': {
    'type': 'string'
},

'collectingAddress': {
    'type': 'string'
},

'origin': {
    'type': 'string'
},

'sourceHospital': {
    'type': 'string'
},

'birthDate': {
    'type': 'string'
},

'apotropus': {
    'type': 'string'
},

'birthCountry': {
    'type': 'string'
},

'language': {
    'type': 'string'
},

'altContactPhone': {
    'type': 'string'
},

'smokes': {
    'type': 'boolean'
},


    'IDNumber': {
        'type': 'string',

    },
    'address': {
        'type': 'string'
    },
    'city': {
        'type': 'string',

    },
    'firstName': {
        'type': 'string',

    },
    'lastName': {
        'type': 'string',

    },
    'mda': {
        'type': 'boolean',

    },
    'comments': {
        'type': 'string',

    },
    'disabilities': {
        'type': 'string',

    },
    'allergies': {
        'type': 'string',

    },
    'foodRestrictions': {
        'type': 'string',

    },
    'guidelines': {
        'type': 'boolean',

    },
    'sentToKabala': {
        'type': 'boolean',

    },
    'realeased': {
        'type': 'boolean',

    }
    



    }


schema = {
    "type": "object",
    "properties": prop,

    "required":
        [
         'IDNumber',
         
         'firstName',
         'lastName',
         'city',
         'address',
         'phone', 
            'releaseDate',
            'hafnayaTime',
            'arrivingTime',
            'collectingDate',
            'receptionTime',
         ]
}