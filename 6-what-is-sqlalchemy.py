# official website: https://www.sqlalchemy.org/
# before using SQLAlchemy, you need to install it:
# pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, Table
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()


# the ORM version of the table creation:
# Table('users', Base.metadata,
#       Column('id', Integer, primary_key=True),
#       Column('name', String),
#       Column('age', Integer)
#       )
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return f"User ID: {self.id}, Name: {self.name}, Age: {self.age}"


# the RAW SQL of the table creation:
# CREATE TABLE users (
#     id INTEGER NOT NULL,
#     name VARCHAR,
#     age INTEGER,
#     PRIMARY KEY (id)
# )
# run from the python code with the following line with (for example) psycopg2:
# cursor.execute('CREATE TABLE users (id INTEGER NOT NULL, name VARCHAR, age INTEGER, PRIMARY KEY (id))')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='John Doe', age=30)
second_user = User(name='Jane Doe', age=25)
session.add(new_user)
session.commit()

users = session.query(User).all()
for user in users:
    print(f'User ID: {user.id}, Name: {user.name}, Age: {user.age}')

first_user = session.query(User).first()
print(first_user)
session.close()
