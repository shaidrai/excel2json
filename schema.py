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
    'contactPhone': {
        'type': 'string',

    },

    # Dates

    'hafnayaDate': {
        'type': 'string',

    },
    'hafnayaTime': {
        'type': 'string',

    },
    'receptionDate': {
        'type': 'string',

    },
    'receptionTime': {
        'type': 'string',

    },
    'collectingDate': {
        'type': 'string',

    },
    'arrivingTime': {
        'type': 'string',

    },
    'releaseDate': {
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

'age': {
    'type': 'number'
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


    'id': {
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
         'id',
         
         'firstName',
         'lastName',
         'city',
         'address',
         'phone']
}