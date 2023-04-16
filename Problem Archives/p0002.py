


def fibsum(limit):
    """
    returns the sum of even elements of the fibonacci series starting with 1 and 2
    arguments:
      limit - maximum value of the fibonacci series term till which the sum is evaluated
    """
    prev = 1
    curr = 2
    x = prev + curr
    sum = 2
    while(x<limit):
        x = prev + curr
        sum = sum + (x if x%2==0 else 0)
        prev = curr
        curr = x
    return sum
    

if __name__ == "__main__":
    print(fibsum(4000000))
