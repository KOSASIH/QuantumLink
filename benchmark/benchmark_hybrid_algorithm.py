import time
import numpy as np
from quantumlink.algorithms import hybrid_algorithm

def benchmark_hybrid_algorithm(input_size):
    """
    Benchmark the performance of the hybrid quantum-classical algorithm.
    """
    # Generate random input data of the specified size
    input_data = np.random.rand(input_size)

    # Measure the execution time of the algorithm
    start_time = time.time()
    result = hybrid_algorithm(input_data)
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    return execution_time

if __name__ == "__main__":
    # Define input sizes to benchmark
    input_sizes = [100, 500, 1000, 5000]

    # Benchmark the algorithm for each input size
    for input_size in input_sizes:
        execution_time = benchmark_hybrid_algorithm(input_size)
        print(f"Input size: {input_size}, Execution time: {execution_time} seconds")
