from app.models.data import Auto

# mein auto = platzhalter für exhte Objekt(BMW)

# service function / verarbeitung


def bewerte_auto(mein_auto: Auto):
    # control flow / conditional logic
    if mein_auto.km < 50:
        ergebnis = "Neues Auto"
    elif mein_auto.marke == "BMW":
        ergebnis = "Gute Marke"
    else:
        ergebnis = "Schlechtes Auto"

    # return status
    print(ergebnis)
