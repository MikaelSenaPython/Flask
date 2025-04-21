# CONEXÃO DA ROTA PRINCIPAL COM O ARQUIVO PRINCIPAL(main.py)
from flask import Flask

app = Flask(__name__)


from estudo.views import homepage
