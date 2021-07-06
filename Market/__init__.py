from flask import Flask, config, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'f0800ff0f810279f66c95968'
db = SQLAlchemy(app)



from Market import routes