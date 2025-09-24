#!/usr/bin/env python3
"""
Parse FISPACT-II output for key metrics.
"""

import re, sys, json

if len(sys.argv) < 2:
    print("Usage: parse_fispact.py <fispact_output.txt>")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    data = f.read()

# Extract contact dose
dose_match = re.search(r"CONTACT DOSE RATE.*?(\d+\.\d+E?[+-]?\d*)", data, re.DOTALL)
contact_dose = float(dose_match.group(1)) if dose_match else None

# Extract waste class
waste_class = "LLW" if "low level waste" in data.lower() else "FAIL"

summary = {
    "contact_dose_1d_mSv/h": contact_dose,
    "waste_class": waste_class
}

print(json.dumps(summary, indent=2))
