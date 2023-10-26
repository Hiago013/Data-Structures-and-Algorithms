import matplotlib.pyplot as plt
import numpy as np
from Dictionary import Dictionary

LENGTH = 50

def main():
    plt.style.use('seaborn')
    basic_operation_count = np.zeros(LENGTH)
    length_input = np.arange(1, LENGTH + 1)   

    for version in range(5):
        my_dict = Dictionary(version)
        for target in range(LENGTH):
            # Insert values into the dictionary
            for key in range(target+1):
                my_dict.insert(key, 10)

            # Clean up the reset counters
            my_dict.reset_counters()

            # Get a value from the dictionary
            my_dict.get(target)
            
            # Record the basic operation count
            basic_operation_count[target] = my_dict.get_basic_operation()

            # Clean up the dictionary and reset counters
            my_dict.clean()
            my_dict.reset_counters()

        # Plot the basic operation count
        plt.plot(length_input, basic_operation_count)
    plt.legend(['Static', 'Singlylinkedlist', 'Singlylinkedlistv2', 'Singlylinkedlistv3', 'Doublylinkedlist'])
    plt.xlabel("Tamanho da Entrada")
    plt.ylabel("Execuções da Operação Básica")
    plt.tight_layout()
    plt.savefig("all_lists.png", dpi = 600)
    plt.show()

if __name__ == "__main__":
    main()
