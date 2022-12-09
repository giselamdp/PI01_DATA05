
from fastapi import FastAPI
from routes.rout import user


app = FastAPI(title = 'Rep Stream',
              description='Reportes analisis uso de plataforma streaming',
              version='1.0.1')

app.include_router(user)






