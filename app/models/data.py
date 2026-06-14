from pydantic import BaseModel


class Auto(BaseModel):  # class / data model
    # Es gibt einen Datentyp namens Mensch

    baujahr: int
    marke: str
    km: int  # Text
    preis: int
