from src.infra.config import *
from src.infra.db_entities import *
from src.main.utils import hash_password
from src.main.config import app, api

db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)

with DBConnectionHandler() as db:
    try:
        #new_user = Users(name='admin', role=1, email='admin@suzy.com', password=hash_password('admin'))
        #db.session.add(new_user)
        db.session.commit()
    except Exception as ex:
        print(ex)
        db.session.rollback()
    finally:
        db.session.close()

if __name__ == "__main__":
    api.init_app(app)
    app.run(host='0.0.0.0')