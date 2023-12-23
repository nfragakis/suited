import argparse

def fibonacci(term_n):
    # The first two terms of the Fibonacci sequence are 0 and 1.
    if term_n == 0:
        return 0
    elif term_n == 1:
        return 1

    # Initialize the list with the first two Fibonacci numbers.
    output = [0, 1]
    
    # Start the loop from the third term.
    for x in range(2, term_n + 1):
        # Append the sum of the last two elements in the list.
        output.append(output[x - 1] + output[x - 2])

    # Return the last element in the list.
    return output[-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Fibonacci number at a given term.')
    parser.add_argument('term', type=int, help='The term at which to calculate the Fibonacci number.')

    args = parser.parse_args()
    term_n = args.term

    print(fibonacci(term_n))