from fastapi import FastAPI
import gunicorn

app = FastAPI()

@app.get("/")
def read_root():
  return "Hello World!"
