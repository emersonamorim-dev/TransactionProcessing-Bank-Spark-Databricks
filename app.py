from flask import Flask
from endpoints.transactions import transactions


app = Flask(__name__)
app.register_blueprint(transactions, url_prefix='/transactions')

if __name__ == '__main__':
    app.run(debug=True)
