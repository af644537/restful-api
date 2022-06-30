from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask (__name__)
api = Api(app)
CORS()

user = {} #variaabel global

class User(Resource):
    def get(self):
        return user

    def post(self):
        nama = request.form ['nama']
        kelas = request.form ['kelas']
        user['nama'] = nama
        user['kelas'] = kelas
        respon = {'psn': 'data nya masokk'}
        return respon


api.add_resource(User,'/user',methods=['GET','POST'])

if __name__ == '__main__':
    app.run(debug=True)