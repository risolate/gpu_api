from fastapi import FastAPI
from model import GenerationModel, Hatespeech
import uvicorn

app = FastAPI()
model = GenerationModel()


@app.post("/purificate")
async def generation(hatespeech: Hatespeech):

    sentence = hatespeech.dict()["sentence"]
    purificated = model.purification(sentence)

    return {"purificated": purificated}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=30001, reload=True)
