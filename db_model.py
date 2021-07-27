'''
2021/07/27 test mariadb
'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:happyclick@127.0.0.1:3306/happyclick")
Base = declarative_base()
Base.metadata.create_all(engine)

class Userdata(Base):
    __tablename__ = 'userdata'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=100))
    password = sqlalchemy.Column(sqlalchemy.String(length=100))

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def addUser(id, name, password):
    newUser = Userdata(id=id, name=name, password=password)
    session.add(newUser)
    session.commit()

def selectAll():
    userdata = session.query(Userdata).all()
    for data in userdata:
        print(data.name + ' ' + data.password)

addUser(000000, "tsmc", "tsmc")
selectAll()