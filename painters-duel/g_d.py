def filter(fact):
    def inner_func(func):
        def wrapper(*arg):
            return (v for v in func(*arg) if v % fact)
        return wrapper
    return inner_func

@filter(2)
def gen_seq(max):
    for x in range(max):
        yield x

for p in gen_seq(30):
    print(p, end=", ")
    
