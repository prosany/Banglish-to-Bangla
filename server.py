from fastapi import FastAPI
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = FastAPI()

@app.get("/transliterate")
def transliterate_text(text: str):
    try:
        bangla_text = transliterate(text, sanscript.ITRANS, sanscript.BENGALI)
        return {"original": text, "transliterated": bangla_text}
    except Exception as e:
        return {"error": str(e)}

