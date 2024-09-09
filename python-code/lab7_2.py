import os

class ClassNotFoundException(Exception):
    """Custom exception to simulate Java's ClassNotFoundException"""
    pass

def load_class(class_name):
    """Simulate loading a class in Python."""
    available_classes = ["ExistingClass1", "ExistingClass2"]  # List of available classes

    if class_name not in available_classes:
        raise ClassNotFoundException(f"Class '{class_name}' not found.")
    else:
        print(f"Class '{class_name}' loaded successfully.")

def read_file(file_name):
    """Simulate reading a file and handling EOFError."""
    try:
        with open(file_name, 'rb') as file:
            while True:
                byte = file.read(1)  # Read one byte at a time
                if not byte:  # If byte is empty, it's the end of the file
                    raise EOFError
                print(byte.decode('utf-8'), end="")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except EOFError:
        print("\nEnd of file reached.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example 1: Simulating ClassNotFoundException
    try:
        load_class("NonExistentClass")  # This will raise ClassNotFoundException
    except ClassNotFoundException as e:
        print(f"ClassNotFoundException occurred: {e}")

    # Example 2: Simulating EOFError (End of file)
    print("\nSimulating EOFError:")
    read_file("nonexistent.txt")  # This will attempt to open a non-existent file
