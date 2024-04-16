def compose_func(f,g):
    def compose_function(x):
        return f(g(x))
    return compose_function
def square(x):
    return x**2
def double(x):
    return x*2
composed_func = compose_func(square,double)
result = composed_func(3)
print(result)
