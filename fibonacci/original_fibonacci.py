import argparse

def fibonacci( term_n ):
    if term_n == 1:
       return 1

    # This list is initialized with one element, but it should be initialized with two elements [0, 1]
    #  because the Fibonacci sequence starts with 0 and 1.
    output = [1]
    
    # This is an infinite loop because x is never incremented. 
    # We need to increment x at the end of the loop.
    x=0
    while x < term_n:
        # This line will result in an index error if x is 0 because there's no element at index -1.
        # We need to start the loop from x = 2 and initialize the output list with the first two Fibonacci numbers.
        # Also, this line tries to modify the existing element at index x, but we should append the new element to the list.
        output[x] = output[x] + output[x - 1]

    # This line will result in an index error for term_n > 1 because the output list has only one element.
    # We need to return the last element in the list, not the element at index term_n.
    return output[term_n]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Fibonacci number at a given term.')
    parser.add_argument('term', type=int, help='The term at which to calculate the Fibonacci number.')

    args = parser.parse_args()
    term_n = args.term

    print(fibonacci(term_n))
