respuestascorrectas=0
respuestasincorrectas=0
respuestasenblanco=0

respuestascorrectas=int(input("Dime las correctas"))
respuestasincorrectas=int(input("Dime las incorrectas"))
respuestasenblanco=int(input("Dime las blancas"))

puntuacion_de_las_correctas=respuestascorrectas*5
puntuacion_de_las_incorrectas=respuestasincorrectas*-1
puntuacion_de_las_blancas=respuestasenblanco*0

puntuaciontotal=puntuacion_de_las_correctas+puntuacion_de_las_incorrectas+puntuacion_de_las_blancas
print(puntuaciontotal)