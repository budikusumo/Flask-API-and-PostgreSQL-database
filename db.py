from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (create_engine, MetaData)


db = SQLAlchemy()

DefaultConfig = {'user': 'taqiem','password': 'taqiem','host': 'localhost','port': 5432,'database': 'postgres',}
ClientConfig = {'user': 'taqiem','password': 'taqiem','host': 'localhost','port': 5432,'database': 'xxx','encoding': 'SQL_ASCII',}

URIFormat = "postgresql://{user}:{password}@{host}:{port}/{database}"
DefaultURI = (URIFormat.format(**DefaultConfig))
ClientURI = (URIFormat.format(**ClientConfig))
engine_default = create_engine(DefaultURI)

def setup_module():
    conn = engine_default.connect()
    conn.execute("COMMIT")
    conn.execute("CREATE DATABASE {} WITH OWNER = {} ENCODING = {} TEMPLATE = template0 TABLESPACE = pg_default".format(ClientConfig['database'], ClientConfig['user'], ClientConfig['encoding']))
    conn.close()