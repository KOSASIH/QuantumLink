# Import QuantumLink module for post-quantum cryptography
from quantumlink.cryptography import post_quantum_crypto

# Define the message to be encrypted
message = "Hello, Quantum!"

# Encrypt the message using post-quantum cryptography
encrypted_message, decrypted_message = post_quantum_crypto(message)

# Print the encrypted and decrypted messages
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
