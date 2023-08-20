import numpy as np
import scipy.optimize as opt
import numpy_financial as npf

# Paramètres du projet
investissement_initial = 2580000000
annees = 20
taux_actualisation = 0.04

# Fonction pour calculer le VAN
def calcul_van(tarification, nombre_utilisateurs):
    flux_de_caisse = [-investissement_initial]
    cash_flow = 0
    for an in range(1, annees+1):
        cash_flow = cash_flow + nombre_utilisateurs * tarification / ((1 + taux_actualisation) ** an)
    van = cash_flow - investissement_initial
    return van

# Fonction objectif pour l'optimisation
def objectif(x):
    tarification, nombre_utilisateurs = x
    return -calcul_van(tarification, nombre_utilisateurs)  # Négatif car on veut maximiser

# Contraintes
contrainte1 = {'type': 'ineq', 'fun': lambda x: investissement_initial - x[0] * x[1]}  # Contrainte budgétaire

# Valeurs initiales
x0 = [30, 5500000]  # Valeurs initiales pour tarification et nombre d'utilisateurs

# Exécution de l'optimisation
result = opt.minimize(objectif, x0, constraints=contrainte1)

# Affichage des résultats
tarification_optimale, nombre_utilisateurs_optimal = result.x
print("Tarification optimale:", tarification_optimale)
print("Nombre d'utilisateurs optimal:", nombre_utilisateurs_optimal)
print("VAN optimal:", -result.fun)  # Convertir en positif


