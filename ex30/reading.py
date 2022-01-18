import os
from flask import Flask, jsonify, request, abort, make_response
from flask.helpers import stream_with_context
import mysql.connector
import json
# @audit-ok com erro no eliminar 

app = Flask(__name__)
reading_list = []
reading_counter = 0


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='sensors'
)

cur = mydb.cursor()

cur.execute("""SELECT * FROM reading""")
out = cur.fetchall()
for linha in out:
    dicionario = {
        'idReading': linha[0],
        'idSensor': linha[1],
        'tomestamp': linha[2],
        'value': linha[3],
    }
    reading_list.append(dicionario)

cur.execute('SELECT max(idReading) from reading')
reading_counter = cur.fetchone()[0]



# função para manipular erros por código ou classe de exceção.
@app.errorhandler(404)
def not_found(error):
    return jsonify({'Erro': 'Não encontrada'}), 404

# função para devolver lista de coisas
@app.route('/reading/', methods=['GET'])
def get_things():
    return jsonify({'reading': reading_list})

# função para devolver uma das coisas, por ID
@app.route('/reading/<int:reading_id>', methods=['GET'])
def get_thing(reading_id):
    for read in reading_list:
        if read['idReading'] == reading_id:
            return jsonify(read)
    else:
        abort(404)

# função para adicionar uma coisa à lista
@app.route('/reading/', methods=['POST'])
def create_thing():
    if not request.json or \
            'idSensor' not in request.json or \
            'tomestamp' not in request.json or \
            'value' not in request.json:
        abort(400)

    global reading_counter
    reading_counter += 1
    thing = {
        'idReading': reading_counter,
        'idSensor': request.json['idSensor'],
        'tomestamp': request.json['tomestamp'],
        'value': request.json['value']
    }
    reading_list.append(thing)

    try:
        sql = "INSERT INTO reading (idSensor, timestamp, value) VALUES ({}, {}, {})".format(
            str(request.json['idSensor']), 
            str(request.json['tomestamp']), 
            str(request.json['value'])
            )
        cur.execute(sql)
        mydb.commit()
    except (Exception, TypeError) as e:
        return {
            'message': "Bad request!",
            'status': 400,
            # 'Error': str(e),
        }, 400

    # status code 201, which HTTP defines as the code for "Created". See https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    # a resposta de um POST deve ter o suficiente para saber duas coisas:
    # - Que a criação aconteceu(código 201)
    # - Onde encontrar a coisa nova (neste caso bastaria devolver o novo id)
    return jsonify(thing), 201


@app.route('/reading/<int:reading_id>', methods=['PUT'])
def update_thing(reading_id):

    if not request.json:
        abort(400) # 400 Bad Request

    for read in reading_list:
        if read['idReading'] == reading_id:
            # print(request.json.get('idSensor', read['idSensor']))
            read['idSensor'] = request.json.get('idSensor', read['idSensor'])
            read['tomestamp'] = request.json.get('tomestamp', read['tomestamp'])
            read['value'] = request.json.get('value', read['value'])
            try:
                sql = "UPDATE reading SET idSensor = {}, timestamp = {}, value = {} WHERE idReading = {}".format(
                    str(read['idSensor']), 
                    str(read['tomestamp']), 
                    str(read['value']), 
                    str(reading_id)
                    )
                cur.execute(sql)
                mydb.commit()
            except (Exception, TypeError) as e:
                return {
                    'message': "Bad request!",
                    'status': 400,
                    # 'Error': str(e),
                }, 400
            return jsonify(read)
    else:
        abort(404)  # 404 	Not Found


@app.route('/reading/<int:reading_id>', methods=['DELETE'])
def delete_thing(reading_id):
    for read in reading_list:
        if read['idReading'] == reading_id:
            try:
                reading_list.remove(read)
                sql = "DELETE FROM reading WHERE idReading = "+ str(reading_id)
                cur.execute(sql)
                mydb.commit()
                return jsonify(read)
            except Exception as e:
                return {
                    'message': "Bad request!",
                    'status': 400,
                    # 'Error': str(e),
                }, 400
    else:
        abort(404)



if __name__ == '__main__':

    app.run(debug=True, port=int(os.environ.get('PORT', 8080)))
