import matplotlib.pyplot as plt
import numpy as np
import math

# === Settings ===
sigfigs = 4

# === Constants ===
pionRestMassEnergy = 139.57 # MeV
c = 3.0 * 10**8 # m/s

# === Local Constants ===
q = 1.6 * 10**(-19) # Coulombs
B = 1.4 # T

# === Measurement Data === 
pionRadiiCentral = [[0.60, 0.65], [1.10, 0.28], [0.60, 1.10], [0.60, 0.75], [0.41, 0.75]] # measurement central values
pionRadiiError = [[0.05,0.05],[0.05,0.05],[0.05,0.05],[0.05,0.05],[0.05,0.05]] # measurement errors

# initial fractional measurement error
pionRadiiFractionalError = [[0,0],[0,0],[0,0],[0,0],[0,0]] # measurement errors

# === Momenta List (to-fill) ===
pionMomentaCentral = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]] # to calculate
pionMomentaError = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
pionMomentaFractionalError = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


# === MOMENTA CALCULATION ===
# TODO
# - significant figures
for event in range(len(pionMomentaCentral)):
    for pion in range(2):
        # calculate central value
        pionMomentaCentral[event][pion] = 2.988 * 10**2 * pionRadiiCentral[event][pion] * B

        # propogate error (direct, fractional)
        pionRadiiFractionalError[event][pion] = pionRadiiError[event][pion]/pionRadiiCentral[event][pion] # measurement errors
        pionMomentaFractionalError[event][pion] = pionRadiiFractionalError[event][pion]
        pionMomentaError[event][pion] = pionMomentaFractionalError[event][pion] * pionMomentaCentral[event][pion]

        # pionMomentaError[event][pion] = round(pionMomentaError[event][pion],sigfigs)
        # pionMomentaCentral[event][pion] = round(pionMomentaCentral[event][pion],sigfigs)

# === Display momenta calculations ===
for i in range(len(pionMomentaCentral)):
        print("Event", i, "... (+)Pion:", pionMomentaCentral[i][0], "+/-", pionMomentaError[i][0],", (-)Pion:", pionMomentaCentral[i][1], "+/-", pionMomentaError[i][1])


# === REST MASS CALCULATION === 
pionTotalEnergyCentral = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

kaonMomentaCentral = [0,0,0,0,0]
kaonMomentaError = [0,0,0,0,0]
kaonMomentaFractionalError = [0,0,0,0,0]

kaonTotalEnergyCentral = [0,0,0,0,0]
kaonEnergyError = [0,0,0,0,0]
kaonEnergyFractionalError = [0,0,0,0,0]

kaonRestMassEnergyCentral = [0,0,0,0,0]
kaonRestMassEnergyError = [0,0,0,0,0]
kaonRestMassEnergyFractionalError = [0,0,0,0,0]

for event in range(len(kaonMomentaCentral)):
    # A. calc pions total energies (MeV)
    pionTotalEnergyCentral[event][0] = math.sqrt(pionRestMassEnergy**2 + pionMomentaCentral[event][0]**2)
    pionTotalEnergyCentral[event][1] = math.sqrt(pionRestMassEnergy**2 + pionMomentaCentral[event][1]**2)
    
    print("Pions E_tot (MeV)... (+):", pionTotalEnergyCentral[event][1], " (-): ", pionTotalEnergyCentral[event][0])

    # propogate error from pion momenta to kaon momentum
    # kaonMomentaError[event] = math.sqrt(pionMomentaError[event][0]**2 + pionMomentaError[event][1]**2)
    # kaonMomentaFractionalError[event] = kaonMomentaError[event]/kaonMomentaCentral[event]

    # B. calc kaon total energy (MeV)
    kaonTotalEnergyCentral[event] = pionTotalEnergyCentral[event][0] + pionTotalEnergyCentral[event][1]

    print("K0",event,"total energy (MeV)",kaonTotalEnergyCentral[event])

    # C. calc kaon momentum (MeV/c)
    kaonMomentaCentral[event] = pionMomentaCentral[event][0] + pionMomentaCentral[event][1]

    print("K0",event,"momentum (MeV/c)",kaonMomentaCentral[event])
    
    # D. calc kaon rest mass energy (MeV)
    kaonRestMassEnergyCentral[event] = math.sqrt(kaonTotalEnergyCentral[event]**2 - (kaonMomentaCentral[event])**2)
    kaonTotalEnergyCentral[event]**2 - (kaonMomentaCentral[event]*c)**2
    
    print("K0",event,"rest mass energy (MeV): ", kaonRestMassEnergyCentral[event])


# === UNCERTAINTY OF P / SUM OF PERPENDICULAR MOMENTA ===
perpendicularMomenta = [0,0,0,0,0]

# Angle Measurements
pionAngleCentral = [[38,26],[26,63],[48,30],[43,42],[63,63]]
pionAngleError = [[4,4],[9,9],[4,4],[4,4],[30,30]]

for event in range(len(pionMomentaCentral)):
    perpendicularMomenta[event] = pionMomentaCentral[event][0]*math.cos(math.radians(pionAngleCentral[event][0])) + pionMomentaCentral[event][1]*math.cos(math.radians(pionAngleCentral[event][1]))

    print("Event",event,"Total perp. momentum:",perpendicularMomenta[event])
    
    # propogate error through (11) with formula, to get kaon rest mass energy error
    kaonRestMassEnergyError[event] = abs((perpendicularMomenta[event] *  (-perpendicularMomenta[event])/math.sqrt(kaonTotalEnergyCentral[event]**2 - perpendicularMomenta[event]**2)))

    print("k0 error:",kaonRestMassEnergyError[event])


# === RELAVISTIC FLIGHT TIME OF K0 CALCULATION

kaonVelocityCentral = [0,0,0,0,0]
kaonPathLength = [0.022,0.003,0.014,0.812,0.001]

for event in range(len(kaonVelocityCentral)):
    kaonVelocityCentral[event] = ((kaonMomentaCentral[event]/kaonTotalEnergyCentral[event]))*c

    print("K0",event,"velocity:",kaonVelocityCentral[event])

    print("K0",event,"galilean flight time:",kaonPathLength[event]/kaonVelocityCentral[event])

    gamma = 1/math.sqrt(1-((kaonVelocityCentral[event]**2)/c**2))
    print("gamma:",gamma)
    print("K0",event,"relativistic flight time:",gamma*kaonPathLength[event]/kaonVelocityCentral[event])

