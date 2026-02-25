from flask import Flask

app = Flask(__name__)


from carcompanyblog.core.views import core #import blueprint
from carcompanyblog.error_pages.handlers import error_pages #import blueprint

app.register_blueprint(core)
app.register_blueprint(error_pages)