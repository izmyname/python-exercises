# Even numbers generator

def even_gen():
    for n in range(101):
        if n % 2 == 0:
            yield(n)
            
even_nums = even_gen()

while True:
    try:
        print(next(even_nums))
    except StopIteration:
        break
    
# Generator expression
def odd_cubes():
    
    yield from (n**3 for n in range(21) if n % 2 == 1)
    
cubes = odd_cubes()

while True:
    try:
        print(next(cubes))
    except StopIteration:
        break

# File readline simulator
def readline_sim():
    line1 = "Þann gel ek þér fyrstan"
    line2 = "- þann kveða fjölnýtan"
    line3 = "Þann gól Rindi Rani, -"
    line4 = "At þú of öxl skjótir"
    line5 = "Því er þér atalt þykkir;"
    line6 = "Sjalfr leið þú sjalfan þik"
    
    yield line1
    yield line2
    yield line3
    yield line4
    yield line5
    yield line6

traust = readline_sim()

while True:
    try:
        print(next(traust))
    except StopIteration:
        break