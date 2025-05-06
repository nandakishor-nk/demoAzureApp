from fastapi import FastAPI
import unicorn

app = FastAPI()

@app.get("/")
def read_root():
  return "Hello World!"
