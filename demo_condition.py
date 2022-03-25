def multi(n1, n2):
    product = n1*n2
    if product >= 1000:
        return product
    else:
        return n1+n2

    n1=20
    n2=30

    result = multi(n1, n2)
    print("The result is", result)



