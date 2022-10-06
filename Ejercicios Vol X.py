examen1=0
examen2=0
examen3=0
examenfinal=0
trabajofinal=0
examen1=(int)(input("La nota del primer examen es:\n"))
examen2=(int)(input("La nota del segundo examen es:\n"))
examen3=(int)(input("La nota del tercer examen es:\n"))
examenfinal=(int)(input("La nota del examen final es:\n"))
trabajofinal=(int)(input("La nota del trabajo final es:\n"))
print("La media de los examenes parciales es",(examen1+examen2+examen3)/3)
examenesparciales=(examen1+examen2+examen3)/3
print("La nota final es "((examenesparciales*0.55)+(examenfinal*0.3)+(trabajofinal*0.15)/3))
