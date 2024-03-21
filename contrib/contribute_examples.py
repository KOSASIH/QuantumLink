# Import necessary modules
from quantumlink.examples import Example

# Define a function to contribute new examples
def contribute_example(example_name, description, code_snippet):
    # Create a new Example object with the provided details
    example = Example(name=example_name, description=description, code_snippet=code_snippet)
    # Save the example to the examples directory
    example.save()
    print(f"Example '{example_name}' contributed successfully.")

# Example usage of the contribute_example function
if __name__ == "__main__":
    # Example details for the new example
    example_name = "Custom Quantum Key Distribution"
    description = "Demonstrates a custom quantum key distribution protocol."
    code_snippet = """
# Insert code snippet demonstrating the custom quantum key distribution protocol here
    """
    # Contribute the new example
    contribute_example(example_name, description, code_snippet)
