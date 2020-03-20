import numpy as np
import os
from flask import Flask, request, send_from_directory, Response
import os
import json
import excel2json
import requests

AllowedFiles = ['xlsx', 'csv']

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000


def check_ex(filename):
    return filename.split('.')[-1] in AllowedFiles

#def save_file()

app = Flask(__name__)
url = 'https://fieldhospital.azurewebsites.net/infecteds/excel'

@app.route('/', methods=['GET'])
def test():
    return json.dumps({"test":'1'})


@app.route('/api/excel2json', methods=['POST'])
def upload_file():
    try:
        print('req')
        file = request.files['file']
        token = request.headers['Authorization']
        
        if check_ex(file.filename):
            full_path = './' + file.filename
            file.save(full_path)

            data = excel2json.formatExcel(full_path)
            print(data)
            data = json.dumps(data)
            res = requests.post(url, data= data, headers= {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'close',
             'Content-Length': '16',
             'Content-Type': 'application/json',
             'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
             'X-Request-Id': 'xx-xx-xx', 'Authorization': token })

            print(res)
            print(res.content)
            if res.status_code == 200 or res.status_code == 201:

            	return json.dumps({'success': True})

            else:
            	res = Response(json.dumps({'success': False, 'error': str(res.content)}), status=res.status_code)

    except Exception as e:
        print(e)
        res = Response(json.dumps({'success': False, 'error': str(e)}), status=400)
        return res


if __name__ == "__main__":
    app.run(port=port, debug=True)

