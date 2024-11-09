# arrays.py

class Array:
    def __init__(self, capacity, fill_value=None):
        # Initialize the array with the given capacity and fill_value
        self.items = [fill_value] * capacity

    def __str__(self):
        # Return a string representation of the array (useful for testing)
        return str(self.items)


# Testing the Array class
if __name__ == "__main__":
    # Create an array instance with a capacity of 5 and filled with 0
    arr = Array(5, 0)
    
    # Print the array
    print(arr)  

