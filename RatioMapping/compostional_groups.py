import matplotlib.pyplot as plt

# Conversion factors from oxides to elements (approximate)
conversion_factors = {
    'SiO2': 0.4675,  # Si = 28.0855 / (28.0855 + 2 * 15.9994)
    'Al2O3': 0.5293, # Al = 2 * 26.9815 / (2 * 26.9815 + 3 * 15.9994)
    'FeO': 0.7773,   # Fe = 55.845 / (55.845 + 15.9994)
    'MgO': 0.6031,   # Mg = 24.305 / (24.305 + 15.9994)
    'CaO': 0.7147    # Ca = 40.078 / (40.078 + 15.9994)
}

# Data for Apollo missions with oxide values converted to elemental wt%
# Apollo 11
SiO2_A11 = [43,41.3,41.9,42.16,41.79,45.2,43.5]
Al2O3_A11 = [13,13.7,13.55,13.6,13.44,14,13.7]
FeO_A11 = [16,15.8,15.94,15.34,15.91,14.4,14.7]
MgO_A11 = [8,8,7.82,7.76,7.66,7.55,7.67]
CaO_A11 = [12,12.5,12.08,11.94,12.14,11.3,12]

Si_A11 = [x * conversion_factors['SiO2'] for x in SiO2_A11]
Al_A11 = [x * conversion_factors['Al2O3'] for x in Al2O3_A11]
Fe_A11 = [x * conversion_factors['FeO'] for x in FeO_A11]
Mg_A11 = [x * conversion_factors['MgO'] for x in MgO_A11]
Ca_A11 = [x * conversion_factors['CaO'] for x in CaO_A11]

# Apollo 12
SiO2_A12 = [47.3,47.97,48.35,48.1,47.3]
Al2O3_A12 = [17.8,17.57,18.1,17.6,17.1]
FeO_A12 = [15,15.11,14.1,14.5,15.3]
MgO_A12 = [10.9,9.89,9.4,10.2,13.4]
CaO_A12 = [10.4,10.53,10.7,12.2,10.6]

Si_A12 = [x * conversion_factors['SiO2'] for x in SiO2_A12]
Al_A12 = [x * conversion_factors['Al2O3'] for x in Al2O3_A12]
Fe_A12 = [x * conversion_factors['FeO'] for x in FeO_A12]
Mg_A12 = [x * conversion_factors['MgO'] for x in MgO_A12]
Ca_A12 = [x * conversion_factors['CaO'] for x in CaO_A12]

# Apollo 14
SiO2_A14 = [45.7,46.5,45.4,45.3]
Al2O3_A14 = [15.6,15.5,15.4,15.2]
FeO_A14 = [13.4,13.3,13.2,13.1]
MgO_A14 = [11.2,11.1,11,10.9]
CaO_A14 = [10.1,10,9.9,9.8]

Si_A14 = [x * conversion_factors['SiO2'] for x in SiO2_A14]
Al_A14 = [x * conversion_factors['Al2O3'] for x in Al2O3_A14]
Fe_A14 = [x * conversion_factors['FeO'] for x in FeO_A14]
Mg_A14 = [x * conversion_factors['MgO'] for x in MgO_A14]
Ca_A14 = [x * conversion_factors['CaO'] for x in CaO_A14]

# Apollo 15
SiO2_A15 = [50.3,50.7,50.1,50.5]
Al2O3_A15 = [16.7,16.8,16.9,17]
FeO_A15 = [12.1,12.3,12.2,12.4]
MgO_A15 = [8.5,8.6,8.7,8.8]
CaO_A15 = [11.9,12,12.1,12.2]

Si_A15 = [x * conversion_factors['SiO2'] for x in SiO2_A15]
Al_A15 = [x * conversion_factors['Al2O3'] for x in Al2O3_A15]
Fe_A15 = [x * conversion_factors['FeO'] for x in FeO_A15]
Mg_A15 = [x * conversion_factors['MgO'] for x in MgO_A15]
Ca_A15 = [x * conversion_factors['CaO'] for x in CaO_A15]

# Apollo 17
SiO2_A17 = [48.3,48.5,48.1,48.4]
Al2O3_A17 = [16.3,16.5,16.4,16.6]
FeO_A17 = [13.8,13.7,13.6,13.5]
MgO_A17 = [9.3,9.2,9.4,9.5]
CaO_A17 = [11.2,11.3,11.1,11]

Si_A17 = [x * conversion_factors['SiO2'] for x in SiO2_A17]
Al_A17 = [x * conversion_factors['Al2O3'] for x in Al2O3_A17]
Fe_A17 = [x * conversion_factors['FeO'] for x in FeO_A17]
Mg_A17 = [x * conversion_factors['MgO'] for x in MgO_A17]
Ca_A17 = [x * conversion_factors['CaO'] for x in CaO_A17]

# Plot all data in a single figure
plt.figure(figsize=(10, 8))

# Define color map for each mission
colors = {
    "Apollo 11": 'black',
    "Apollo 12": 'red',
    "Apollo 14": 'blue',
    "Apollo 15": 'green',
    "Apollo 17": 'purple'
}

# Plot each element pair against Al
plt.scatter(Al_A11, Si_A11, color=colors["Apollo 11"], label="Apollo 11 - Si", marker='o')
plt.scatter(Al_A11, Fe_A11, color=colors["Apollo 11"], label="Apollo 11 - Fe", marker='x')
plt.scatter(Al_A11, Mg_A11, color=colors["Apollo 11"], label="Apollo 11 - Mg", marker='s')
plt.scatter(Al_A11, Ca_A11, color=colors["Apollo 11"], label="Apollo 11 - Ca", marker='d')

plt.scatter(Al_A12, Si_A12, color=colors["Apollo 12"], label="Apollo 12 - Si", marker='o')
plt.scatter(Al_A12, Fe_A12, color=colors["Apollo 12"], label="Apollo 12 - Fe", marker='x')
plt.scatter(Al_A12, Mg_A12, color=colors["Apollo 12"], label="Apollo 12 - Mg", marker='s')
plt.scatter(Al_A12, Ca_A12, color=colors["Apollo 12"], label="Apollo 12 - Ca", marker='d')

plt.scatter(Al_A14, Si_A14, color=colors["Apollo 14"], label="Apollo 14 - Si", marker='o')
plt.scatter(Al_A14, Fe_A14, color=colors["Apollo 14"], label="Apollo 14 - Fe", marker='x')
plt.scatter(Al_A14, Mg_A14, color=colors["Apollo 14"], label="Apollo 14 - Mg", marker='s')
plt.scatter(Al_A14, Ca_A14, color=colors["Apollo 14"], label="Apollo 14 - Ca", marker='d')

plt.scatter(Al_A15, Si_A15, color=colors["Apollo 15"], label="Apollo 15 - Si", marker='o')
plt.scatter(Al_A15, Fe_A15, color=colors["Apollo 15"], label="Apollo 15 - Fe", marker='x')
plt.scatter(Al_A15, Mg_A15, color=colors["Apollo 15"], label="Apollo 15 - Mg", marker='s')
plt.scatter(Al_A15, Ca_A15, color=colors["Apollo 15"], label="Apollo 15 - Ca", marker='d')

plt.scatter(Al_A17, Si_A17, color=colors["Apollo 17"], label="Apollo 17 - Si", marker='o')
plt.scatter(Al_A17, Fe_A17, color=colors["Apollo 17"], label="Apollo 17 - Fe", marker='x')
plt.scatter(Al_A17, Mg_A17, color=colors["Apollo 17"], label="Apollo 17 - Mg", marker='s')
plt.scatter(Al_A17, Ca_A17, color=colors["Apollo 17"], label="Apollo 17 - Ca", marker='d')

# Labeling and formatting
plt.xlabel('Al (wt%)')
plt.ylabel('Elemental Concentration (wt%)')
plt.title('Elemental Concentrations vs Al Content for Apollo Samples')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Missions and Elements")
plt.grid(True)
plt.tight_layout()
plt.show()
