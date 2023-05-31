def compute(f,s,lim):
    """
    returns the sum of even elements of the fibonacci series starting with 1 and 2
    arguments:
      f - first number of the fibonacci series
      s - second number of the fibonacci series
      limit - maximum value of the fibonacci series term till which the sum is evaluated
    """
    sum = 0
    while (s<lim):
        if(not s%2):
            sum+=s
        s = f + s
        f = s - f
    return sum

if __name__ == "__main__":
    print(compute(1,2,4000000))
