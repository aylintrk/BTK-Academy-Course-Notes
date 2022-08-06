from fastapi import FastAPI

app= FastAPI()

app.get("/")

def root():
    return "hello world"

app.get("/topla")

def topla(x:int,y:int):
    return x+y