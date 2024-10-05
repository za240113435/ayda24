def add(a,b):
    return a+b
x=eval(input("inserta numero  a"))
y=eval(input("inserta numero  b"))
txt = "Suma {:.2f}"
print(txt.format(add(x,y)))
