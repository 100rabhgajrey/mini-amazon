from flask import Flask

app = Flask('Amazon', template_folder='./amazon/templates')

from amazon import api
