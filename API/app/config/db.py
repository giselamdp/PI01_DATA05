from sqlalchemy import create_engine, MetaData


engine = create_engine("mysql+pymysql://root:Andrea25%@host.docker.internal:3306/peliculas")



meta= MetaData()


