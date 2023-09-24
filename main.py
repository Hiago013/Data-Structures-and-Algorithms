import matplotlib.pyplot as plt
import numpy as np
from Dictionary import Dictionary

LENGTH = 100
VERSION = 0

def main():
    basic_operation_count = np.zeros(LENGTH)
    my_dict = Dictionary(VERSION)
    
    for target in range(1, LENGTH):
        # Insert values into the dictionary
        for key in range(target):
            my_dict.insert(key, 10)
        
        # Get a value from the dictionary
        my_dict.get(target - 1)
        
        # Record the basic operation count
        basic_operation_count[target] = my_dict.get_basic_operation()
        
        # Clean up the dictionary and reset counters
        my_dict.clean()
        my_dict.reset_counters()
    
    # Plot the basic operation count
    plt.plot(basic_operation_count)
    plt.show()

if __name__ == "__main__":
    main()
