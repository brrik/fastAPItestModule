from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # CORS
import datetime

app = FastAPI()
#handler = Mangum(app)

counts = [0,0,0,0]
retData = {}

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
    global counts
    global retData
    retData = makeRetData(counts)
    return retData


@app.get("/add/{item_id}")
def add_item(item_id: int):
    global counts
    global retData
    counts[item_id]  += 1
    retData = makeRetData(counts)
    return retData


@app.get("/reset")
def reset_items():
    global counts
    global retData
    counts = [0,0,0,0]
    retData = makeRetData(counts)
    return retData

def makeRetData(origData: list):
    modData = {
        "c1": origData[0],
        "c2": origData[1],
        "c3": origData[2],
        "c4": origData[3]
    }

    return modData
