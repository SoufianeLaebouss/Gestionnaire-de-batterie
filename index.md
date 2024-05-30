---
title: Gestionnaire de Batterie
layout: default
---

# Gestion de Décharge de Pile avec INA3221

## Introduction

Dans ce projet, j'ai développé un système de gestion de décharge de pile utilisant le module INA3221, qui permet de mesurer la tension de bus et la tension de shunt (représentant le courant de décharge) à travers une liaison I2C. L'objectif principal était de configurer le module INA3221, de lire ses valeurs périodiquement, de les enregistrer via une liaison série vers un PC, puis de les analyser pour obtenir des informations telles que la résistance interne de la pile, la tension en fonction du temps, le courant en fonction du temps, l'énergie totale fournie par la pile, ainsi que la caractéristique tension-courant de la pile.

## Utilisation du Module INA3221

J'ai créé deux fonctions principales pour interagir avec le module INA3221 :

1. **Configuration du Module**: Cette fonction permet de configurer les paramètres du module INA3221, tels que la plage de mesure, la précision et le taux de conversion. Ces paramètres sont cruciaux pour garantir des mesures précises et fiables.

2. **Lecture des Mesures**: Après la configuration, cette fonction lit périodiquement les valeurs de tension de bus et de tension de shunt à travers une liaison I2C. Ces valeurs sont ensuite utilisées pour calculer le courant de décharge de la pile.

![Module INA3221](chemin/vers/module_ina3221.png)

## Gestion du Temps avec un Timer

Pour lire les mesures périodiquement, j'ai utilisé un timer pour déclencher une interruption toutes les 1 seconde. À chaque interruption, la fonction de lecture des mesures est appelée pour récupérer les données du module INA3221.

![Timer](chemin/vers/timer.png)

## Difficultés Rencontrées

Une difficulté majeure que j'ai rencontrée était la gestion du temps dans un environnement temps réel. Initialement, j'ai tenté d'implémenter la lecture des mesures dans une tâche, mais j'ai rapidement réalisé que le temps dérivait, ce qui aurait faussé mes mesures. Pour résoudre ce problème, j'ai opté pour l'utilisation d'un timer pour garantir une précision temporelle constante.

![Difficultés](chemin/vers/difficultes.png)

## Traitement des Données

Une fois les mesures récupérées, je les envoie via une liaison série vers un PC. Sur le PC, un programme reçoit les données et les enregistre dans un fichier. J'ai ensuite utilisé des outils comme Excel pour analyser ces données. J'ai délimité les données de tension et de courant, puis j'ai calculé la résistance interne de la pile en fonction du temps.

![Traitement des Données](chemin/vers/traitement_donnees.png)

## Analyse des Données

En utilisant les données enregistrées, j'ai pu tracer plusieurs graphiques pour mieux comprendre les performances de la pile :

1. **Tension en Fonction du Temps**: Ce graphique montre comment la tension de la pile évolue au fil du temps, ce qui peut donner des informations sur sa décharge.

![Tension en Fonction du Temps](chemin/vers/tension_temps.png)

2. **Courant en Fonction du Temps**: Ce graphique illustre le courant de décharge de la pile au fil du temps, ce qui permet de visualiser sa performance.

![Courant en Fonction du Temps](chemin/vers/courant_temps.png)

3. **Énergie Totale Fournie par la Pile**: En intégrant le produit de la tension et du courant sur la période de décharge, j'ai calculé l'énergie totale fournie par la pile.

![Énergie Totale](chemin/vers/energie_totale.png)

4. **Caractéristique Tension-Courant de la Pile**: Ce graphique met en évidence la relation entre la tension et le courant de décharge de la pile, ce qui peut être utile pour évaluer ses performances dans différentes conditions.

![Caractéristique Tension-Courant](chemin/vers/caracteristique.png)

## Conclusion

Le système de gestion de décharge de pile que j'ai développé avec le module INA3221 offre une solution robuste pour évaluer les performances des piles. En combinant une configuration précise du module, une gestion efficace du temps et une analyse approfondie des données, j'ai pu obtenir des informations précieuses sur la résistance interne de la pile, son comportement en fonction du temps et son efficacité énergétique. Ce projet illustre l'importance de la surveillance et de l'analyse des performances des piles pour une utilisation optimale dans diverses applications.