import numpy as np
import os
from flask import Flask, request, send_from_directory, Response
import os
import json
import excel2json
import requests

AllowedFiles = ['xlsx', 'csv']

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTcwNDkxMDE5ZDBhOTI3ZDBiMGZiNmMiLCJpYXQiOjE1ODQ0MTk2OTJ9.ucHMyz9VR-MMyLTyodXfpS53wBB-ekFVvppi4H-yK6E'
def check_ex(filename):
    return filename.split('.')[-1] in AllowedFiles

#def save_file()

app = Flask(__name__)
url = 'http://10.0.3.161:5000/infecteds/excel'

@app.route('/', methods=['GET'])
def test():
    return json.dumps({"test":'1'})


@app.route('/api/excel2json', methods=['POST'])
def upload_file():
    try:
        print('req')
        file = request.files['file']
        headers = request.headers
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
            return json.dumps({'success': True})
    except Exception as e:
        print(e)
        res = Response(json.dumps({'success': False, 'error': str(e)}), status=400)
        return res


if __name__ == "__main__":
    app.run(port=5000, debug=True)

