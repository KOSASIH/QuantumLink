import unittest
from quantumlink.key_distribution import generate_quantum_key

class TestQuantumKeyDistribution(unittest.TestCase):
    def test_generate_quantum_key_with_valid_length(self):
        # Test case with valid key length
        key_length = 128
        quantum_key = generate_quantum_key(key_length)
        self.assertEqual(len(quantum_key), key_length, "Unexpected length for generated quantum key")

    def test_generate_quantum_key_with_invalid_length(self):
        # Test case with invalid key length
        key_length = -1
        with self.assertRaises(ValueError):
            generate_quantum_key(key_length)

    def test_generate_quantum_key_with_zero_length(self):
        # Test case with zero key length
        key_length = 0
        quantum_key = generate_quantum_key(key_length)
        self.assertEqual(len(quantum_key), key_length, "Unexpected length for generated quantum key")

if __name__ == '__main__':
    unittest.main()
