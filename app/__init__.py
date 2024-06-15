from flask import Flask
from config import Config, config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import pyrebase
from firebase import firebase







app = Flask(__name__)
app.config.from_object(Config)
    
    
app.app_context().push()


migrate = Migrate(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'


firebasse = firebase.FirebaseApplication('https://authpyblog-default-rtdb.firebaseio.com/', None)

firebas = pyrebase.initialize_app(config)
authen = firebas.auth()
db = firebas.database()


from . import routes
app.register_blueprint(routes.auth)
app.register_blueprint(routes.blog)

