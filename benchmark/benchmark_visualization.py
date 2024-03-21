import matplotlib.pyplot as plt
import numpy as np

def visualize_benchmarks(algorithms, execution_times):
    """
    Visualize benchmark results using a bar plot.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, execution_times, color='skyblue')
    plt.xlabel('Algorithms and Protocols')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Benchmark Results')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example benchmark results (replace with actual data)
    algorithms = ['Hybrid Algorithm', 'Quantum Key Distribution', 'Post-Quantum Cryptography']
    execution_times = [10.2, 5.7, 7.8]

    # Visualize benchmark results
    visualize_benchmarks(algorithms, execution_times)
