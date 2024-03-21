import unittest
from quantumlink.cryptography import post_quantum_crypto

class TestPostQuantumCryptography(unittest.TestCase):
    def test_post_quantum_crypto_encryption_decryption(self):
        # Test case for encryption and decryption
        message = "Hello, Quantum!"
        encrypted_message, decrypted_message = post_quantum_crypto(message)
        self.assertNotEqual(encrypted_message, message, "Encryption failed: Encrypted message is the same as the original message")
        self.assertEqual(decrypted_message, message, "Decryption failed: Decrypted message does not match the original message")

    def test_post_quantum_crypto_signature_verification(self):
        # Test case for digital signature generation and verification
        message = "Hello, Quantum!"
        signature = post_quantum_crypto.generate_signature(message)
        self.assertTrue(post_quantum_crypto.verify_signature(message, signature), "Signature verification failed: Signature does not match the message")

if __name__ == '__main__':
    unittest.main()
