from app.models.data import Auto
from app.core.processor import bewerte_auto

BMW = Auto(  # Object / Instance
    baujahr=1,
    marke="BMW",
    km=4,
    preis=12000
)

# function call / invocation
bewerte_auto(BMW)
