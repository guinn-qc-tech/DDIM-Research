import random

# --- PARAMETERS ---
p_initial = 0.055  # Phase A: Early Universe (CMB)
drag_factor = 0.08 # Phase B: 8% "Thinning" due to expansion/drag
p_local = p_initial * (1 - drag_factor) # The "Local" effective probability
runs = 1000 # Increased for higher precision

def simulate_universe(p):
    dimension = 1
    while True:
        dimension += 1
        if random.random() < p:
            return dimension

# --- RUN PHASE A (EARLY) ---
results_a = [simulate_universe(p_initial) for _ in range(runs)]
avg_a = sum(results_a) / runs
expected_a = 1 / p_initial

# --- RUN PHASE B (LOCAL) ---
results_b = [simulate_universe(p_local) for _ in range(runs)]
avg_b = sum(results_b) / runs
expected_b = 1 / p_local

# --- THE "TENSION" CALCULATION ---
# We treat the change in dimensional depth as the "Hubble Tension" ratio
tension_ratio = (avg_b / avg_a) - 1

print(f"--- DDIM HUBBLE TENSION ANALYSIS ---")
print(f"Phase A (Early/CMB) p: {p_initial:.4f} | Expected E[X]: {expected_a:.2f} | Simulated Avg: {avg_a:.2f}")
print(f"Phase B (Local) p:     {p_local:.4f} | Expected E[X]: {expected_b:.2f} | Simulated Avg: {avg_b:.2f}")
print("-" * 40)
print(f"Calculated 'Hubble Tension' (Expansion Shift): {tension_ratio * 100:.2f}%")
print("-" * 40)

if 5.0 < (tension_ratio * 100) < 10.0:
    print("STATUS: SUCCESS. Shift aligns with observed ~7-9% Hubble Tension.")
else:
    print("STATUS: CALIBRATION REQUIRED. Adjust drag_factor to match observed data.")