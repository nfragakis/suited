import argparse

def fibonacci(term_n):
    if term_n == 1:
       return 1

    output = [1]
    x=0
    while x < term_n:
        output[x] = output[x] + output[x - 1]

    return output[term_n]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Fibonacci number at a given term.')
    parser.add_argument('term', type=int, help='The term at which to calculate the Fibonacci number.')

    args = parser.parse_args()
    term_n = args.term

    print(fibonacci(term_n))
