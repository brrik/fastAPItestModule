from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # CORS
import datetime

app = FastAPI()
#handler = Mangum(app)

counts = [0,0,0,0]
free_list = []
retData = {}
freeRetData = {}

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_root():
    global counts
    global retData
    retData = makeRetData(counts)
    return retData


@app.get("/add/{item_id}")
async def add_item(item_id: int):
    global counts
    global retData
    counts[item_id]  += 1
    retData = makeRetData(counts)
    return retData

@app.get("/reset")
def reset_items():
    global counts
    global free_list
    global freeRetData
    global retData
    counts = [0,0,0,0]
    free_list = []
    retData = {
        "c1": 0,
        "c2": 0,
        "c3": 0,
        "c4": 0
    }
    freeRetData = {}
    return retData

@app.get("/result")
def show_result():
    global freeRetData
    global retData
    global counts
    sumRet = 0
    for i in counts:
        sumRet = sumRet + i
    
    if sumRet == 0:
        print(freeRetData)
        return freeRetData
    else:
        print(retData)
        return retData

@app.get("/free/{postData}")
async def freeform_add_item(postData :str):
    global free_list
    global freeRetData
    free_list.append(postData)
    freeRetData = makeFreeRetData(free_list)
    return freeRetData

def makeRetData(origData: list):
    modData = {
        "c1": origData[0],
        "c2": origData[1],
        "c3": origData[2],
        "c4": origData[3]
    }

    return modData

def makeFreeRetData(origData :list):
    modData = {}
    for i in range(len(origData)):
        modData["data" + str(i)] = origData[i]
    
    return modData
