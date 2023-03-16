import sqlalchemy

#configuração do sqlalchemy para conexão com o banco de dados e criação da sessão
engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/desafiotce")

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()