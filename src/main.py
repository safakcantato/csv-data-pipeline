from app.models.data import Auto
from app.core.processor import bewerte_auto

BMW = Auto(
    baujahr=2020,
    marke="BMW",
    km=40,
    preis=20000
)

result = bewerte_auto(BMW)

print("RESULT:", result)
