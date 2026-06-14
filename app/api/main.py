from fastapi import FastAPI
from app.models.data import Auto
from app.core.processor import bewerte_auto

app = FastAPI()


@app.post("/auto")
def auto_bewerten(auto: Auto):

    ergebnis = bewerte_auto(auto)

    return {
        "marke": auto.marke,
        "bewertung": ergebnis
    }
