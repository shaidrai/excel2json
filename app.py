
import os
from flask import Flask, request, send_from_directory, Response
import os
import json
import excel2json
import requests
from flask_cors import CORS, cross_origin

AllowedFiles = ['xlsx', 'csv']

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 80


def check_ex(filename):
    return filename.split('.')[-1] in AllowedFiles

#def save_file()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/', methods=['GET'])
@cross_origin()
def test():
    return json.dumps({"test":'1'})


@app.route('/api/excel2json', methods=['POST'])
@cross_origin()
def upload_file():
    try:
        print('req')
        file = request.files['file']

        print('request')
        
        if check_ex(file.filename):
            full_path = './' + file.filename

            # Saving the file
            file.save(full_path)

            # Formating the file to json
            data = excel2json.formatExcel(full_path)



            # Deleting the file
            os.remove(full_path)

            print("finished formating")
            data = json.dumps(data, ensure_ascii=False).encode('utf8')

            data = data.decode()

            #print(data)

            res = Response(data, status=200)
            return res
                

    except Exception as e:
        print(e)
        res = Response(json.dumps({'success': False, 'error': str(e)}), status=400)
        return res




@app.route('/api/json2excel', methods=['POST'])
@cross_origin()
def upload_json():
    print("x")
    try:
        data = json.loads(request.form['data'])

        print(data)

        path = excel2json.formatJson(data)

        res =  json.dumps({"path": path})

        return res
        
        #excel2json.formatJson()

    except Exception as e:
        #print(e)
        print("sssss")
        print(e)
        res = Response(json.dumps({'success': False, 'error': str(e)}), status=400)
        return res


@app.route('/api/getExcelFile/<path:path>')
@cross_origin()
def root(path):
    print(path)
    return send_from_directory('./public', path)

if __name__ == "__main__":
    app.run(port=port, debug=True)

#last version

