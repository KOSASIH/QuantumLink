import time
import numpy as np
from quantumlink.cryptography import post_quantum_crypto

def benchmark_post_quantum_cryptography(message_size):
    """
    Benchmark the performance of post-quantum cryptography operations.
    """
    # Generate random message of the specified size
    message = np.random.bytes(message_size)

    # Measure the time taken to perform encryption and decryption
    start_time = time.time()
    encrypted_message, decrypted_message = post_quantum_crypto.encrypt_decrypt_message(message)
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    return execution_time

if __name__ == "__main__":
    # Define message sizes to benchmark
    message_sizes = [1000, 5000, 10000]

    # Benchmark post-quantum cryptography for each message size
    for message_size in message_sizes:
        execution_time = benchmark_post_quantum_cryptography(message_size)
        print(f"Message size: {message_size} bytes, Execution time: {execution_time} seconds")
