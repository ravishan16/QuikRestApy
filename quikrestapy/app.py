from quikrestapy import *
from flask import Flask, Blueprint
from flask_restplus import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from quikrestapy.api import api
from quikrestapy.api.users import user_ns
from quikrestapy.models import db

print os.path.join(os.path.dirname(__file__),'logging.cfg')
logging.config.fileConfig(os.path.join(os.path.dirname(__file__),'logging.cfg'))
log = logging.getLogger(__name__)
print log


def initapp():
    app = Flask(__name__)
    app.config.from_pyfile('server.cfg')
    print app.config['SERVER_NAME']
    print app.config['SWAGGER_UI_DOC_EXPANSION']
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    print blueprint
    print api
    api.init_app(blueprint)
    api.add_namespace(user_ns)
    app.register_blueprint(blueprint)
    db.init_app(app)
    return app

if __name__ == "__main__":

    app = initapp()
    print app
    print "Starting"
    app.run(debug=True)
