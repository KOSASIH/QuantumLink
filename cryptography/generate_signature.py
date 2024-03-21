def generate_signature(message):
    """
    Generate a digital signature for a message using quantum-safe signature schemes.
    
    Parameters:
    message (str): Message to be signed.
    
    Returns:
    digital_signature (str): Digital signature for the message using quantum-safe signature schemes.
    """
    # Digital signature generation using quantum-safe signature schemes
    digital_signature = sign(message)
    return digital_signature
