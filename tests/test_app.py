from app import app


def test_sante_repond_ok():
    client = app.test_client()
    reponse = client.get("/sante")
    assert reponse.status_code == 200
    assert reponse.get_json()["statut"] == "ok"


def test_stations_sans_base():
    client = app.test_client()
    donnees = client.get("/stations").get_json()
    assert donnees["source"] == "memoire"
    assert len(donnees["stations"]) == 4


def test_alertes_seuil_deux_velos():
    client = app.test_client()
    donnees = client.get("/alertes").get_json()
    assert donnees["source"] == "memoire"
    noms = [s["nom"] for s in donnees["alertes"]]
    assert "Place du Marche" in noms
    for station in donnees["alertes"]:
        assert station["velos_disponibles"] <= 2
