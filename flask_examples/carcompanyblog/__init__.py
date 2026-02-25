from flask import Flask

app = Flask(__name__)


from carcompanyblog.core.views import core #import blueprint
app.register_blueprint(core)
