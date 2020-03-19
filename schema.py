# data format schema
prop = {'room': {
    'type': 'number',

},
    'daysLeft': {
        'type': 'number'
    },
    'conversation': {
        'type': 'boolean',

    },
    'underAge': {
        'type': 'boolean',

    },
    'allergys': {
        'type': 'string',
    },
    'shabat': {
        'type': 'boolean',

    },
    'phone': {
        'type': 'string',

    },
    'replacedPhone': {
        'type': 'string',

    },
    'foodSensitivity': {
        'type': 'string'
    },
    'releaseDate': {
        'type': 'string',

    },
    'hafnayaDate': {
        'type': 'string',

    },
    'arrivingTime': {
        'type': 'string',

    },
    'registrationTime': {
        'type': 'string',

    },
    'IDNumber': {
        'type': 'string',

    },
    'fullAddress': {
        'type': 'string'
    },
    'city': {
        'type': 'string',

    },
    'street': {
        'type': 'string',

    },
    'houseNumber': {
        'type': 'number',

    },
    'firstName': {
        'type': 'string',

    },
    'lastName': {
        'type': 'string',

    },
    'HMO': {
        'type': 'string',

    },
    'MDA': {
        'type': 'boolean',

    },
    'status': {
        'type': 'string',

    },
    'serialNumber': {
        'type': 'number',

    }}
schema = {
    "type": "object",
    "properties": prop,

    "required":
        ['room',
         'conversation',
         'underAge',
         'shabat',
         'phone',
         'replacedPhone',
         'releaseDate',
         'hafnayaDate',
         'IDNumber',
         'city',
         'arrivingTime',
         'registrationTime',
         'street',
         'houseNumber',
         'firstName',
         'lastName',
         'HMO',
         'MDA',
         'status']
}