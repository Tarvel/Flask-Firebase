import os

class Config:
    SECRET_KEY = '48a89ef0b9a63e63dc8a5ca21fc1871d'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    # 'postgresql://postgres:08060110993@localhost/flask_eCommerce'
    # postgresql://flask_ecommerce_81dp_user:KD5OFXHSHIOdhpmoZ48j8zC1B2gyvX1J@dpg-cotb936g1b2c73de8qeg-a/flask_ecommerce_81dp
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.abspath('static/profile_pic')
    DEBUG = True

config = {
    'apiKey': "AIzaSyAUxp29-Otuqkg_-iT4pITcpGNMGP47uPA",
  'authDomain': "authpyblog.firebaseapp.com",
  'projectId': "authpyblog",
  'storageBucket': "authpyblog.appspot.com",
  'messagingSenderId': "873960858821",
  'appId': "1:873960858821:web:553168a362d4865b967cac",
  'measurementId': "G-XV0QD0S9EF",
  'databaseURL': "https://authpyblog-default-rtdb.firebaseio.com/User_Detail"
}