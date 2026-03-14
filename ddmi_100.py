import random

def run_ddim_simulation(p_threshold=0.05, max_dim=200):
    # Dimension 1 is locked as the Original Existence
    for dim in range(2, max_dim + 1):
        if random.random() <= p_threshold:
            return dim
    return max_dim # Reached the limit without a phase transition

# Configuration
total_runs = 100
results = []
probability = 0.055

print(f"--- DDIM 100-Run Statistical Analysis ---")
print(f"Parameters: Probability of Finiteness (p) = {probability}")
print(f"Calculating {total_runs} independent universal lifespans...\n")

for i in range(total_runs):
    outcome = run_ddim_simulation(p_threshold=probability)
    results.append(outcome)

# Calculate Statistics
average_dim = sum(results) / total_runs
earliest = min(results)
latest = max(results)

# Display Summary
print("--- SUMMARY REPORT ---")
print(f"Total Runs: {total_runs}")
print(f"Mathematical Expected Value (E[X]): 18.18")
print(f"Simulated Average Dimension: {average_dim}")
print(f"Earliest Compilation: Dimension {earliest}")
print(f"Deepest Chaos Survivor: Dimension {latest}")
print("-" * 30)

# Distribution visualization (simple)
print("\nDistribution Profile:")
ranges = [(2,10), (11,20), (21,40), (41,200)]
for low, high in ranges:
    count = len([r for r in results if low <= r <= high])
    print(f"Dimensions {low}-{high}: {'#' * (count // 2)} ({count} universes)")