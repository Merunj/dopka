import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Departament(SqlAlchemyBase):
    __tablename__ = 'departament'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, 
                              index=True, unique=True, nullable=True)
    member = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
