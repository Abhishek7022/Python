a = "Hello, World!"
b = 'This is a test and you passed'
print (a+b)

def numSum(n1, n2):
    n1 = int(input())
    n2 = int(input())
    if (n1 < n2):
        return ('n2 is greater than n1')
    else:
        return ('n1 is greater than n2')

print (numSum(a, b))
