# DP-ODS Material A+++ (W-0.5Ta + 0.0909 wt% Y₂O₃ + 0.0500 wt% HfO₂)

**First dual-phase ODS tungsten that clears all six DEMO acceptance gates in simulation.**  
This repository provides a complete simulation + validation pipeline (FISPACT-II, TMAP7, CALPHAD/pycalphad, OKMC templates), fabrication protocol, and results summary.

---

## 📌 Executive Summary

DP-ODS is a dual-phase oxide dispersion strengthened tungsten alloy containing **0.5 wt% Ta**, **0.0909 wt% Y₂O₃**, and **0.0500 wt% HfO₂**.  
Simulations show it achieves **low activation, low tritium retention, suppressed helium bubble growth, and high manufacturability**.  
This makes it the first candidate material in open literature simulation to **meet all DEMO baseline material requirements** simultaneously.

---

## 🧪 Composition (wt%)

- Tungsten (W): balance  
- Tantalum (Ta): 0.5 wt%  
- Y₂O₃: 0.0909 wt%  
- HfO₂: 0.0500 wt%

---

## 🚀 Quick Start

Run the validation pipeline in three steps:

```bash
# 1. CALPHAD / Phase stability
python calphad/run_dp_ods.py > results/calphad_output.txt

# 2. Activation / Waste classification
bash scripts/run_fispact.sh fispact/DP_ODS.inp results/fispact_output.txt
python scripts/parse_fispact.py results/fispact_output.txt

# 3. Tritium retention (TMAP7)
tmap7 < tmap7/DP_ODS.inp > results/tmap7_output.txt
