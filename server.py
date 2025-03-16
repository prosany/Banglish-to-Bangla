from fastapi import FastAPI
from bengali.unicode import Avro

app = FastAPI()
converter = Avro()  # Avro phonetic transliteration

@app.get("/transliterate")
def transliterate(text: str):
    bangla_text = converter.convert(text)
    return {"original": text, "transliterated": bangla_text}
