from fastapi import FastAPI
from bengali_transliteration import getTransliteration

app = FastAPI()

@app.get("/transliterate")
def transliterate(text: str):
    bangla_text = getTransliteration(text)
    return {"original": text, "transliterated": bangla_text}

# Run using: uvicorn server:app --host 0.0.0.0 --port 7077
