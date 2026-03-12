#Generators in python
def gen(n):
    for i in range(n):
        yield i*i

# Example usage
g = gen(5)
for value in g:
    print(value)
    
#Generator expressions
squares = (x**2 for x in range(5))
for value in squares:
    print(value)