from fastapi import FastAPI

from backend.config import API_NAME, VERSION

app = FastAPI(

    title=API_NAME,

    version=VERSION

)

@app.get("/")

def home():

    return {

        "status":"online",

        "project":"Autonomous Navigation System"

    }

@app.get("/health")

def health():

    return {

        "server":"ok"

    }
