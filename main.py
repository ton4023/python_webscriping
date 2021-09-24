from fastapi import FastAPI
from scriping import TourismThailand
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    response = tourismThailand.regionDestination()
    return {"regionDestination": response}

@app.get("/theme")
def read_theme():
    response = tourismThailand.themeDestination()
    return {'themeDestination' : response}

if __name__ == "__main__":
    tourismThailand = TourismThailand()  
    uvicorn.run(app, host="0.0.0.0", port=8000)