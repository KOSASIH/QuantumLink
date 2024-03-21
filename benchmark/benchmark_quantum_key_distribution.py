import time
import numpy as np
from quantumlink.key_distribution import generate_quantum_key

def benchmark_quantum_key_distribution(key_length):
    """
    Benchmark the efficiency of quantum key distribution protocols.
    """
    # Measure the time taken to generate a quantum key of the specified length
    start_time = time.time()
    quantum_key = generate_quantum_key(key_length)
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    return execution_time

if __name__ == "__main__":
    # Define key lengths to benchmark
    key_lengths = [128, 256, 512]

    # Benchmark the quantum key distribution protocol for each key length
    for key_length in key_lengths:
        execution_time = benchmark_quantum_key_distribution(key_length)
        print(f"Key length: {key_length} bits, Execution time: {execution_time} seconds")
