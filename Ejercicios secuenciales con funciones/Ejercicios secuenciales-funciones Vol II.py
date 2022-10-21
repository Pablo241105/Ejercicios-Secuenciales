base=0
altura=0
base = (int)(input("Dime la base: \n"))
altura = (int)(input("Dime la altura: \n"))
def area(base,altura):
    return("Esta es el area:",base*altura)

def perimetro(base,altura):
    return("Este es el perimetro",base+altura)

def lista(basde,altura):
    vDatos=[]
    vDatos.append(base)
    vDatos.append(altura)
    return("Esta es la lista: ",vDatos)


print("Esta es el area: ",base*altura)

print("Este es el perimetro: ",base+altura)

print("Esta es la lista",lista(base,altura))
