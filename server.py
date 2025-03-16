from fastapi import FastAPI
from bn_transliterate import BNTransliterate

app = FastAPI()
bn = BNTransliterate()

@app.get("/transliterate")
def transliterate(text: str):
    bangla_text = bn.transliterate(text)
    return {"original": text, "transliterated": bangla_text}
