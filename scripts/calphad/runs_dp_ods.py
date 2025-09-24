#!/usr/bin/env python3
"""
Run CALPHAD phase stability for DP-ODS alloy.
Requires pycalphad and a suitable thermodynamic database (SGTE tungsten alloy).
"""

from pycalphad import Database, equilibrium, variables as v
import numpy as np
import matplotlib.pyplot as plt

# Load database
db = Database("databases/sgte_w.tdb")  # <-- You need SGTE db

# Define system
comps = ["W", "Ta", "Y2O3", "HfO2"]
phases = db.phases.keys()

# Composition (mole fractions approximate)
# Note: convert wt% -> mol fraction
comp = {v.X("Ta"): 0.005, v.X("Y2O3"): 0.000909, v.X("HfO2"): 0.0005}

# Temperature and pressure grid
T = np.linspace(300, 2000, 50)
P = 101325

print("Running equilibrium calculation...")
eq = equilibrium(db, comps, phases, {v.T: T, v.P: P, **comp})

# Plot example: phase fractions vs temperature
plt.figure()
for phase in phases:
    if phase in eq.Phase.values:
        frac = eq.X.sel(vertex=phase).mean(dim="vertex")
        plt.plot(T, frac, label=phase)

plt.xlabel("Temperature (K)")
plt.ylabel("Phase fraction")
plt.legend()
plt.title("DP-ODS Phase Stability")
plt.savefig("results/calphad_phase_fractions.png")
print("Saved results/calphad_phase_fractions.png")
