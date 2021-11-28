from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "postgresql://umraszjslzcuki:ada3fea18f733cf7c87aa891fe861653935c3dc4f7fb77afba6a568d8c4b6d5b@ec2-54-144-165-97.compute-1.amazonaws.com/daocu03v9l1u0e"
        self.session = None

    def get_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
