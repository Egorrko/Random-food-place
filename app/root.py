from flask import Flask
from routes import *

app = Flask(__name__, template_folder='routes/templates', static_folder='routes/static')
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()
