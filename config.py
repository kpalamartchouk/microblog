import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'postgresql://kpalamar:kpalamar@localhost:5432/sandbox'
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
#        'mysql+pymysql://kpalamar:kpalamar@localhost/sandbox'
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
#        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
