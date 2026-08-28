"""velos-api : etat des stations de velos en libre-service."""

import os

from flask import Flask, jsonify

app = Flask(__name__)

# Jeu de donnees de secours, utilise quand aucune base n'est configuree.
STATIONS_SECOURS = [
    {"nom": "Gare Centrale", "quartier": "Centre", "velos_disponibles": 12, "capacite": 20},
    {"nom": "Place du Marche", "quartier": "Centre", "velos_disponibles": 2, "capacite": 15},
    {"nom": "Parc des Sports", "quartier": "Nord", "velos_disponibles": 7, "capacite": 10},
    {"nom": "Universite", "quartier": "Sud", "velos_disponibles": 1, "capacite": 25},
]


def lire_stations():
    """Retourne (stations, source). La source vaut 'postgres' ou 'memoire'."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        return STATIONS_SECOURS, "memoire"

    import psycopg2

    with psycopg2.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT nom, quartier, velos_disponibles, capacite "
                "FROM stations ORDER BY nom"
            )
            lignes = cur.fetchall()

    stations = [
        {"nom": n, "quartier": q, "velos_disponibles": v, "capacite": c}
        for n, q, v, c in lignes
    ]
    return stations, "postgres"


@app.get("/sante")
def sante():
    """Route destinee aux machines, pas aux humains."""
    return jsonify({"statut": "ok", "version": "1.0"})


@app.get("/stations")
def stations():
    donnees, source = lire_stations()
    return jsonify({"source": source, "stations": donnees})


@app.get("/disponibilite")
def disponibilite():
    donnees, source = lire_stations()
    capacite_totale = sum(s["capacite"] for s in donnees)
    if not capacite_totale:
        return jsonify({"source": source, "taux_occupation": None})
    velos = sum(s["velos_disponibles"] for s in donnees)
    taux = round(100 * velos / capacite_totale, 1)
    return jsonify({"source": source, "taux_occupation": taux})


# ---------------------------------------------------------------------------
# A TOI DE JOUER (jalon 3 de l'enonce)
#
# Ajoute ici une route /alertes qui renvoie les stations dont le nombre de
# velos disponibles est inferieur ou egal a 2 (le seuil d'alerte).
# Respecte la forme des reponses ci-dessus : le champ "source" doit y figurer.
# Puis ecris le test correspondant (jalon 4).
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
