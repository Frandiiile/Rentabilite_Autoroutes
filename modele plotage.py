import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy_financial as npf

nombre_simulations = 10000
investissement_initial = 2580000000 # Montant initial investi
annees = 20  # Durée du projet
taux_actualisation = 0.04  # Taux d'actualisation
moyenne_tarification = 31  # Tarification moyenne

# Création d'une distribution de tarifications autour de la moyenne
ecart_type_tarification = 3.055
tarifications = np.random.normal(moyenne_tarification, ecart_type_tarification, nombre_simulations)
# Variation de tarification entre -15% et +15%
pourcentage_variation = np.random.uniform(-0.15, 0.15, nombre_simulations)
tarifications_variation = tarifications * (1 + pourcentage_variation)

# Fonction pour calculer le VAN
def calcul_van(tarification):
    flux_de_caisse = [-investissement_initial]
    for an in range(1, annees+1):
        flux = np.random.uniform(5000000, 6000000) * tarification / (1 + taux_actualisation) ** an
        flux_de_caisse.append(flux)
    
    van = npf.npv(taux_actualisation, flux_de_caisse)
    return van
print("le van est : " ,calcul_van(50))

# Calcul du VAN pour chaque tarification avec variation
vans = [calcul_van(tarif) for tarif in tarifications_variation]

# Variation du VAN par rapport à la tarification moyenne
variation_van = [van - calcul_van(moyenne_tarification) for van in vans]

# Affichage des résultats
print("VAN moyen:", np.mean(vans))
print("Variation du VAN moyen:", np.mean(variation_van))

# Plot de la distribution des variations du VAN
plt.hist(variation_van, bins=30, edgecolor='black')
plt.xlabel('Variation du VAN')
plt.ylabel('Fréquence')
plt.title('Distribution des Variations du VAN')
plt.show()
plt.scatter(tarifications, vans, alpha=0.5)
plt.xlabel('Tarification')
plt.ylabel('VAN')
plt.title('Relation entre Tarification et VAN')
plt.show()
