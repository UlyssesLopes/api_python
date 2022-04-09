from flask import Flask, jsonify, request
import json


app = Flask(__name__)

desenvolvedores = [
    {'nome':'Ulysses',
     'habilidades':['Python', 'Flask'],
     },
    {'nome':'Lopes',
     'habilidades':['Python', 'Django']}
]

# devolve um desenvolvedor pelo id, tambem altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status':'ERRO', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador'
            response = {'status':'ERRO', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro Excluido'})

# lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def listar_desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)