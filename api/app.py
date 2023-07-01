from flask import Flask, redirect, url_for, jsonify, abort, request, render_template

app = Flask(__name__)

headers = {"Content-Type": "application/json; charset=utf-8"}

planosDeEnsino = [
   {'Codigo':'BLU3024','Ano e Semestre':'2023-1', 'Turma':'unica', 'Nome do Professor':'Maiquel de Brito', 'Email': 'maiquel.b@ufsc.br', 
    'Horario e local da aula': 'quarta 13:30 e quinta 15:10 na sala A305','Horario de atendimento': 'terca 10:00 sala C304', 
    'Metodologia': 'Aulas expositivas em quadro, utilizacao de transparencias ou slides, aulas praticas em laboratorio, trabalho pratico extraclasse e estudo dirigido',
 'Avaliacao': '3 trabalhos', 'Recuperacao': 'prova', 'Cronograma': 'Bancos de dados relacionais NoSQL,  Webservices e sistemas SCADA', 
 'Observacoes': 'sujeito a mudancas conforme necessario'},
 {'Codigo':'BLU8002', 'Ano e Semestre':'2023-1', 'Turma':'A', 'Nome do professor':'Mauri Ferrandin', 'Email do professor': 'mauri.ferrandin@ufsc.br', 
  'Horario e local da aula': 'segunda 10:10 e quarta 13:30 na sala A305','Horario do atendimento': 'sexta 13:30 sala A204', 
  'Metodologia': 'Aulas expositivas em quadro, utilizacao de transparencias ou slides, aulas praticas em laboratorio, trabalho pratico extraclasse',
 'Avaliacao': '4 trabalhos e uma prova', 'Recuperacao': 'prova', 'Cronograma': 'Conexionismo, raciocinio incerto, aprendizado por reforco e fuzzy', 
 'Observacoes': 'sujeito a mudancas'},
 
 ]

@app.route('/planosDeEnsino/getplanosDeEnsino', methods=['GET'])
def get_planos():
 return jsonify({'planosDeEnsino':planosDeEnsino})

@app.route('/planosDeEnsino/getplanoDeEnsino/<string:planoDeEnsino_Codigo>', methods=['GET'])
def get_planoDeEnsinoByCodigo(planoDeEnsino_Codigo):
 a = None
 for planoDeEnsino in planosDeEnsino:
    if planoDeEnsino['Codigo'] == planoDeEnsino_Codigo:
        a = planoDeEnsino
 if a == None:
      abort(404)    
 return jsonify(a)

@app.route('/')
def homepage():
    return render_template("base.html")
 

@app.route('/cadastrarplano', methods=["POST", "GET"])
def cadastrarPlano():
   if request.method == "POST":
      planoDeEnsino = {'Codigo': request.form["Codigo"],'Ano e Semestre': request.form["anoeSemestre"],'Turma': request.form["turma"],
                        'Nome do professor': request.form["nomeProfessor"],'E-mail do professor': request.form["email"],
                        'Horario e local das aulas': request.form["horarioELocalAula"],
                        'Horario e local de atendimento ao aluno': request.form["horarioAtendimento"],
                        'Metodologia de ensino': request.form["Metodologia"], 'Avaliação': request.form["avaliacao"],
                        'Recuperacao': request.form["recuperacao"],'Cronograma de aulas': request.form["cronograma"], 
                        'Observacoes': request.form["observacoes"]}
      codigoDiscp = request.form["Codigo"]
      planosDeEnsino.append(planoDeEnsino)
      return redirect(url_for("codigoDiscp", codigoDisc=codigoDiscp))

   else:
      return render_template("cadastrarplano.html")

@app.route("/<codigoDisc>")
def codigoDiscp(codigoDisc):
   return f"<h1>O plano de ensino foi cadastrado com sucesso!</h1>"


if __name__ == "__main__":
  app.run(host = 'localhost', port=8081, debug = True)