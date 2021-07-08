from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user ='fvvneeef'
password ='bcgZ16Q7WdMsKyaJql6mmRmpnovYMQdR'
host ='tuffi.db.elephantsql.com'
database ='fvvneeef'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'admin'

db = SQLAlchemy(app)

class Criptos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    simbolo = db.Column(db.String(10), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)

    def __init__(self,nome,simbolo,imagem_url,descricao):
        self.nome = nome
        self.simbolo = simbolo
        self.imagem_url = imagem_url
        self.descricao = descricao
        
    @staticmethod
    def read_all():
        return Criptos.query.order_by(Criptos.id).all()

    @staticmethod
    def ler(cripto_id):
        return Criptos.query.get(cripto_id);

    def save(self):
        db.session.add(self)
        db.session.commit()

    def atualizar(self, nova_info):
        self.nome = nova_info.nome
        self.simbolo = nova_info.simbolo
        self.imagem_url = nova_info.imagem_url
        self.descricao = nova_info.descricao
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/ler_todos')
def read_all():
    criptos = Criptos.read_all()
    close = db.session.close_all()
    return render_template('ler_todos.html', criptos = criptos, close = close)

@app.route('/adicionar', methods=('GET', 'POST'))
def adicionar():
    id_atribuido = None
    close = db.session.close_all()
    if request.method == "POST":

        form = request.form

        adicionar = Criptos(form['nome'], form['simbolo'], form['imagem_url'], form['descricao'])
        adicionar.save()
        id_atribuido = adicionar.id
        
    return render_template('adicionar.html', id_atribuido = id_atribuido, close = close)

@app.route('/atualizar/<cripto_id>', methods=('GET', 'POST'))
def atualizar(cripto_id):
    atualizado = False
    cripto = Criptos.ler(cripto_id)

    if request.method == 'POST':
        form = request.form
        nova_info = Criptos(form['nome'], form['simbolo'], form['imagem_url'], form['descricao'])
        cripto.atualizar(nova_info)
        atualizado = True
    return render_template('atualizar.html', atualizado = atualizado, cripto = cripto)

@app.route('/ler/<cripto_id>')
def ler(cripto_id):
    cripto  = Criptos.ler(cripto_id)
    print (cripto)
    close = db.session.close_all()
    return render_template('ler.html', cripto = cripto, close = close)



@app.route('/apagar/<cripto_id>')
def apagar(cripto_id):
    cripto = Criptos.ler(cripto_id)
    return render_template('apagar.html', cripto = cripto)

@app.route('/apagar/<cripto_id>/confirmed')
def apagar_confirmado(cripto_id):
    apagado = None
    cripto = Criptos.ler(cripto_id)

    if cripto:
        cripto.delete()
        apagado = True
    return render_template('apagar.html', cripto = cripto, apagado = apagado)



if __name__ == "__main__":
    app.run(debug=True)