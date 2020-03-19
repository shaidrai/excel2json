import numpy as np
import os
from flask import Flask, request, send_from_directory, Response
import os
import json
import excel2json
import requests

AllowedFiles = ['xlsx', 'csv']


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
            data = json.dumps((data))
            print('stack')
            x = requests.post(url, data, headers=headers)
            return json.dumps({'success': True})
    except Exception as e:
        print(e)
        res = Response(json.dumps({'success': False, 'error': str(e), 'nitzan': 'ata homo tauf mipo hofer גנון'}), status=400)
        return res


if __name__ == "__main__":
    app.run(port=5000, debug=True, host= '0.0.0.0')