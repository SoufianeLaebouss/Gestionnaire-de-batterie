import matplotlib.pyplot as plt

Nom = "1_NiMH_1.2V_2500mAh"


# Lire le fichier
with open('donnees_port_serie2_pile11.txt', 'r') as file:
    lines = file.readlines()

# Initialiser les listes pour stocker les tensions, courant, énergie et résistance
tension_shunt = []
tension_bus = []
energie = []
resistance_interne = []
temps = list(range(len(lines)))  # Le temps en secondes basé sur le nombre de lignes
seuil = 1.3

# Variables pour stocker les dernières valeurs prises dans le bloc if
dernier_t1 = None
dernier_t2 = None
V_oc = None  # Tension à vide

# Initialiser l'énergie totale
energie_totale = 0

# Extraire les données et calculer l'énergie et la résistance interne
for i, line in enumerate(lines):
    try:
        t1, t2 = line.strip().split()
        t1 = float(t1)
        t2 = float(t2)
        if t2 < seuil:
            dernier_t1 = t1/10  # Mettre à jour les dernières valeurs
            dernier_t2 = t2
            courant = dernier_t1
            tension = dernier_t2
        else:
            if dernier_t1 is not None and dernier_t2 is not None:
                courant = dernier_t1
                tension = dernier_t2
            else:
                # Si les valeurs ne sont pas encore définies, utiliser les valeurs actuelles
                courant = t1 / 10
                tension = t2
        
        # Mettre à jour V_oc si le courant est très faible
        if courant <=0.5 :
            V_oc = tension
        
        tension_shunt.append(courant)
        tension_bus.append(tension)

        # Calculer l'énergie pour ce pas de temps et l'ajouter à l'énergie totale
        energie_totale += courant * tension
        energie.append(energie_totale)

        # Calculer la résistance interne et l'ajouter à la liste
        if courant != 0 and V_oc is not None:
            R_interne = (V_oc - tension)*10**3 / courant
            if R_interne >=0.1:
                resistance_interne.append(R_interne)
            else:
                resistance_interne.append(None)
        else:
            resistance_interne.append(None)  # Indiquer l'absence de valeur calculable
    except ValueError:
        # Gérer les lignes qui ne peuvent pas être converties
        print(f"Erreur de conversion à la ligne {i + 1}: {line.strip()}")
        continue

# Tracer le courant
plt.figure(1)
plt.plot(temps, tension_shunt, label='I(t)')
plt.xlabel('Temps (s)')
plt.ylabel('Courant (mA)')
plt.title(f"I(t) à travers la pile {Nom}")
plt.savefig(f"Courant_pile_{Nom}.png")
plt.grid(True)
plt.legend()
plt.show()

# Tracer la tension
plt.figure(2)
plt.plot(temps, tension_bus, label='Tension de la pile')
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
plt.title(f"U(t) au borne de la pile {Nom}")
plt.grid(True)
plt.savefig(f"Tension_pile_{Nom}.png")
plt.legend()
plt.show()

# Tracer l'énergie
plt.figure(3)
plt.plot(temps, energie, label='Énergie')
plt.xlabel('Temps (s)')
plt.ylabel('Énergie (mJ)')
plt.title(f"Énergie en fonction du temps de la pile {Nom}")
plt.grid(True)
plt.savefig(f"Energie_pile_{Nom}.png")
plt.legend()
plt.show()

# Tracer la résistance interne
plt.figure(4)
plt.plot(temps, resistance_interne, 'x',label='Résistance interne')
plt.xlabel('Temps (s)')
plt.ylabel('Résistance interne (Ohms)')
plt.title(f"Résistance interne en fonction du temps de la pile {Nom}")
plt.grid(True)
plt.savefig(f"Résistance_interne_pile_{Nom}.png")
plt.legend()
plt.show()


# Tracer la résistance interne
plt.figure(5)
plt.plot(tension_shunt, tension_bus, "x",label='Tension de la pile')
plt.xlabel('Courant (mA)')
plt.ylabel('Tension (V)')
plt.title(f"Caractéristique tension-courant de la pile {Nom}")
plt.xlim([0.4,1])
plt.ylim([0.4,1.05])
plt.grid(True)
plt.savefig(f'Tension_Courant_{Nom}.png') 
plt.legend()

# Afficher les figures
plt.show()