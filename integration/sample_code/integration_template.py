# Import QuantumLink modules for integration
from quantumlink.algorithms import hybrid_algorithm
from quantumlink.key_distribution import generate_quantum_key
from quantumlink.cryptography import post_quantum_crypto

def main():
    # Example integration of QuantumLink functionalities
    
    # 1. Execute a hybrid quantum-classical algorithm
    input_data = [1, 2, 3, 4, 5]
    result = hybrid_algorithm(input_data)
    print("Result of hybrid algorithm execution:", result)
    
    # 2. Generate a quantum key
    key_length = 128
    quantum_key = generate_quantum_key(key_length)
    print("Generated quantum key:", quantum_key)
    
    # 3. Encrypt and decrypt a message using post-quantum cryptography
    message = "Hello, Quantum!"
    encrypted_message, decrypted_message = post_quantum_crypto(message)
    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
