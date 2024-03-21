# Import QuantumLink module for quantum key generation
from quantumlink.key_distribution import generate_quantum_key

# Define the desired length of the quantum key
key_length = 128

# Generate the quantum key using QuantumLink's quantum key distribution protocol
quantum_key = generate_quantum_key(key_length)

# Print the generated quantum key
print("Generated Quantum Key:", quantum_key)
