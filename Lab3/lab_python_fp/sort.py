from math import fabs

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, key=fabs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda i: fabs(i), reverse=True)
    print(result_with_lambda)