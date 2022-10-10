monedadedos=0
monedadeuno=0
monedade50cent=0
monedade20cent=0
monedade10cent=0


monedadedos=(int)(input("Cuantas monedas de 2€ :\n"))
monedadeuno=(int)(input("Cuantas monedas de 1€:\n"))
monedade50cent=(int)(input("Cuantas monedas de 50cent:\n"))
monedade20cent=(int)(input("Cuantas monedas de 20cent:\n"))
monedade10cent=(int)(input("Cuantas monedas de 10cent:\n"))
monedasdeeuro=monedadedos*2+monedadeuno
monedasdecentimos=monedade50cent*50+monedade20cent*20+monedade10cent*10

print("Tienes estos euros",monedasdeeuro,"Tienes estos centimos",monedasdecentimos)
if(monedasdecentimos>=100) :
    print("Sumando los centimos te quedan estos euros ",monedasdeeuro+1,"Y estos centimos " ,monedasdecentimos-100)
    