from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # CORS
import datetime

app = FastAPI()
#handler = Mangum(app)

counts = [0,0,0,0]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {counts}


@app.get("/add/{item_id}")
def add_item(item_id: int):
    counts[item_id]  += 1
    return {counts}


@app.get("/reset")
def reset_items():
    global counts
    counts = [0,0,0,0]
    return
