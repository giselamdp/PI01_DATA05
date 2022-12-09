
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,VARCHAR
from config.db import meta
from config.db import engine


transmision = Table ("transmision",meta, Column("idstream" ,Integer),
Column("tipo", VARCHAR(20)),
Column("title" ,VARCHAR(120)),
Column("release_year" ,Integer) ,
Column("listed_in", VARCHAR(80)),
Column("duracion", Integer ),
Column("TipoDuracion", VARCHAR(10)),
Column("plataforma", VARCHAR(20))
)

actores= Table("actores",meta, Column("idstream" ,Integer),
Column("cast", VARCHAR(100)))

genero= Table("genero",meta, Column("idstream" ,Integer),
Column("listed_in", VARCHAR(50)))


meta.create_all(engine)