
from fastapi import APIRouter
from config.db import engine
from typing import List
from models.modeltrans import transmision,genero,actores
from sqlalchemy import func, select


user= APIRouter()


## Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])

@user.get("/get_max_duration")
def get_max_duration(year:int,plataforma:str,tipoduracion:str):
    with engine.connect() as conn :
        respuesta = conn.execute(select(transmision.c.duracion,transmision.c.title)
                                 .where(transmision.c.release_year==year)
                                 .where(transmision.c.plataforma==plataforma)
                                 .where(transmision.c.TipoDuracion==tipoduracion)
                                 .order_by (transmision.c.duracion.desc()))
        return respuesta.first()
                                                                


 
##Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)
@user.get("/get_count_plataform")
def get_count_plataform(plataforma:str):
    with engine.connect() as conn :
        respuesta2 = conn.execute(select(func.count(transmision.c.tipo),transmision.c.plataforma,transmision.c.tipo)
                                 .where(transmision.c.plataforma==plataforma)
                                 .group_by (transmision.c.tipo,transmision.c.plataforma))
        return respuesta2.fetchall()	
    
##Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
##Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un count de 2099 para la plataforma de amazon.

@user.get("/get_listedin")
def get_listedin(generos:str):
    with engine.connect() as conn :
        respuesta3 = conn.execute(select(func.count(transmision.c.plataforma),transmision.c.plataforma)
                                 .join(genero,transmision.c.idstream==genero.c.idstream)
                                 .where(genero.c.listed_in==generos)
                                 .group_by(transmision.c.plataforma)
                                 .order_by(func.count(transmision.c.plataforma).desc()))

        return respuesta3.first()	

##Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)
 ##Charles Bronson
@user.get("/get_actor")
def get_actor(plataforma:str,year:int):
    with engine.connect() as conn :
        respuesta4 = conn.execute(select(func.count(transmision.c.plataforma),actores.c.cast)
                                 .join(actores,transmision.c.idstream==actores.c.idstream)
                                 .where(transmision.c.plataforma==plataforma)
                                 .where(transmision.c.release_year==year)
                                 .where(actores.c.cast!='No dato')
                                 .group_by(actores.c.cast)
                                 .order_by(func.count(transmision.c.plataforma).desc()))

        return respuesta4.first()	


        