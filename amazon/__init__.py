from flask import Flask

app = Flask('Amazon', template_folder='./amazon/templates')
app.secret_key='some_secret '

from amazon import api
