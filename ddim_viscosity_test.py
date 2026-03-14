import random

# --- PARAMETERS ---
p = 0.055  # Your Anchor
runs = 1000
tail_threshold = 20  # The "Zone of Laws" boundary

def simulate_universe(p):
    dimension = 1
    while True:
        dimension += 1
        if random.random() < p:
            return dimension

# --- RUN STRESS TEST ---
results = [simulate_universe(p) for _ in range(runs)]
tail_count = sum(1 for d in results if d > tail_threshold)
simulated_viscosity = tail_count / runs

print(f"--- DDIM 1,000-RUN VISCOSITY TEST ---")
print(f"Constraint (p): {p}")
print(f"Total Universes Simulated: {runs}")
print(f"Universes trapped in Deep Chaos (> Dim 20): {tail_count}")
print(f"Simulated Informational Viscosity: {simulated_viscosity:.4f}")
print(f"Theoretical Target: {(1-p)**20:.4f}")