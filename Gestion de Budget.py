print("Plateforme de gestion de budget")

from tinydb import TinyDB, Query

db = TinyDB('budget.json')

class Depense:
    def __init__(self, montant, categorie):
        self.montant = montant
        self.categorie = categorie

class Revenu:
    def __init__(self, montant, categorie):
        self.montant = montant
        self.categorie = categorie

def enregistrer_depense(montant, categorie):
    depense = Depense(montant, categorie)
    db.insert({'type': 'depense', 'montant': depense.montant, 'categorie': depense.categorie})

def enregistrer_revenu(montant, categorie):
    revenu = Revenu(montant, categorie)
    db.insert({'type': 'revenu', 'montant': revenu.montant, 'categorie': revenu.categorie})

def calculer_ecart():
    total_depenses = sum(entry['montant'] for entry in db if entry['type'] == 'depense')
    total_revenus = sum(entry['montant'] for entry in db if entry['type'] == 'revenu')
    ecart = total_revenus - total_depenses
    return ecart

# Exemple d'utilisation
enregistrer_depense(50, 'Manger')
enregistrer_depense(30, 'Transport')
enregistrer_revenu(1000, 'Salaire')

print("Ecart:", calculer_ecart())
