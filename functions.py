import RPi.GPIO as GPIO 
from time import sleep
from IPython.display import clear_output

amarillo =12
azul=40
verde = 38
rojo = 13


timbre = 7

GPIO.setwarnings(False) #On désactive les messages d'alerte
GPIO.setmode(GPIO.BOARD)

 #Définit le numéro du port GPIO qui alimente la led



def encender(color,tiempo,color2=33,color3=33,color4=33,color5=33):
    GPIO.setup(color, GPIO.OUT)
    GPIO.setup(color2, GPIO.OUT)
    GPIO.setup(color3, GPIO.OUT)
    GPIO.setup(color4, GPIO.OUT)
    GPIO.setup(color5, GPIO.OUT)
  #  print("encendemos el led durante "+str(tiempo))
    GPIO.output(color,GPIO.HIGH)
    GPIO.output(color2,GPIO.HIGH)
    GPIO.output(color3,GPIO.HIGH)
    GPIO.output(color4,GPIO.HIGH)
    GPIO.output(color5,GPIO.HIGH)
    sleep(tiempo)
   # clear_output(wait=True)      
 #   print("Apagamosel led ")      
    GPIO.output(color,GPIO.LOW)
    GPIO.output(color2,GPIO.LOW)
    GPIO.output(color3,GPIO.LOW)
    GPIO.output(color4,GPIO.LOW)
    GPIO.output(color5,GPIO.LOW)
    #print("**************************************")
    #print("****FIN DE LA INSTRUCCIÓN ENCENDER****")
    #print("**************************************")
    

def sonar(color,tiempo):
    GPIO.setup(color, GPIO.OUT)
   # print("encendemos el led durante "+str(tiempo))
    GPIO.output(color,GPIO.HIGH)
    sleep(tiempo)
    clear_output(wait=True)      
   # print("Apagamosel led ")      
    GPIO.output(color,GPIO.LOW)  
    #print("***********************************")
    #print("****FIN DE LA INSTRUCCIÓN SONAR****")
    #print("***********************************")
    
def tiempo(tiempo):
    sleep(tiempo)
    
ojo1=35
ojo2=26
def VES(ojo):
    GPIO.setup(ojo, GPIO.IN)
    while True:
      try: 
           i= GPIO.input(ojo)
           if i==0:
                print("NO TE VEO¡¡¡¡")
                clear_output(wait=True)
             #   encender(rojo,1)
             #   clear_output()

           else:
                print("TE VEO MACABEO¡¡¡¡")
              #  encender(rojo,1)
                sleep(5)
                clear_output(wait=True)
           sleep(0.2)     
      except KeyboardInterrupt:
                #print("AHORA ESTOY APAGADO")
            #    except KeyboardInterrupt:

                print("AHORA ESTOY APAGADO")
                break
    
            
        

def EMPEZAR():
    

    encender(rojo,1)
    clear_output(wait=True)
    encender(amarillo,1)
    clear_output(wait=True)
    encender(verde,1)
    clear_output(wait=True)
    encender(azul,1)
    clear_output(wait=True)
    sonar(timbre,1)
    clear_output(wait=True)
    encender(rojo,0.5)
    clear_output(wait=True)
    encender(amarillo,0.5)
    clear_output(wait=True)
    encender(verde,0.5)
    clear_output(wait=True)
    sonar(timbre,0.5)
    clear_output(wait=True)
    encender(rojo,0.25)
    clear_output(wait=True)
    encender(amarillo,0.25)
    clear_output(wait=True)
    encender(verde,0.25)
    clear_output(wait=True)
    sonar(timbre,2)
    clear_output(wait=True)
    encender(verde,2,azul,amarillo,rojo,timbre)
    clear_output(wait=True)
    sleep(0.5)
    encender(verde,2,azul,amarillo,rojo,timbre)
    clear_output(wait=True)
    print("   __,_,")
    print("  [_|_/ ")
    print("   //")
    print(" _//    __")
    print("(_|)   |@@|")
    print(" \ \__ \--/ __")
    print("  \o__|----|  |   __")
    print("      \ }{ /\ )_ / _")
    print("      /\__/\ \__O (__")
    print("      (--/\--)    \__/")
    print("      _)(  )(_")
    print("     `---''---`")         
    print("¡YA PODEMOS EMPEZAR CON NUESTRO ROBOT¡")
    


def sonar(color,tiempo):
    GPIO.setup(color, GPIO.OUT)
   # print("encendemos el led durante "+str(tiempo))
    GPIO.output(color,GPIO.HIGH)
    sleep(tiempo)
    clear_output(wait=True)      
   # print("Apagamosel led ")      
    GPIO.output(color,GPIO.LOW)  
    print("***********************************")
    print("****FIN DE LA INSTRUCCIÓN SONAR****")
    print("***********************************")    
    
    
 

def repite(veces,fun1,arg1,fun2=None,arg2=None,fun3=None,arg3=None,fun4=None,arg4=None):
    
    for a in range(0,veces,1):
        fun1(arg1,3)
        sleep(1)
        if fun2==None:
            pass
        else:
            fun2(arg2,3)
        sleep(1)
        if fun3==None:
            pass
        else:
            fun3(arg3,3)
        if fun4==None:
            pass
        else:
            fun4(arg4,3) 
        sleep(1)
        clear_output(wait=True)
        print("****************************************")
        print("**********FIN DEL BUCLE "+str(a)+ "***********")
        print("****************************************")
        
        
def SI(ojo, sens1,sens2=None,sens3=None,sens4=None):
    GPIO.setup(ojo, GPIO.IN)
    GPIO.setup(rojo, GPIO.OUT)
    GPIO.setup(amarillo, GPIO.OUT)
    GPIO.setup(azul, GPIO.OUT)
    GPIO.setup(verde, GPIO.OUT)
    GPIO.setup(timbre, GPIO.OUT)

    while True:
      try: 
           i= GPIO.input(ojo)
           if i==0:
                print("NO TE VEO¡¡¡¡")
                clear_output(wait=True)

                    


           else:
                print("TE VEO MACABEO¡¡¡¡")
                #encender(rojo,1)
                encender(sens1,4) 
                                
                if sens2 ==None:
                    pass
                else:

                    encender(sens2,2)
                    
                if sens3 ==None:
                    pass
                else:
                    encender(sens3,1)
                
                if sens4 ==None:
                    pass
                else:
                    encender(sens4,1)
                sleep(1)
                clear_output(wait=True)
                sleep(5)
           sleep(0.2)
      except KeyboardInterrupt:
                GPIO.output(timbre,GPIO.LOW)
                GPIO.output(rojo,GPIO.LOW)
                GPIO.output(amarillo,GPIO.LOW)
                GPIO.output(azul,GPIO.LOW)
                GPIO.output(verde,GPIO.LOW)
                print("AHORA ESTOY APAGADO")
                break
                
def SINO(ojo, sens1,sens2):
    GPIO.setup(ojo, GPIO.IN)
    GPIO.setup(rojo, GPIO.OUT)
    GPIO.setup(amarillo, GPIO.OUT)
    GPIO.setup(azul, GPIO.OUT)
    GPIO.setup(verde, GPIO.OUT)
    GPIO.setup(timbre, GPIO.OUT)
    while True:
      try: 
           i= GPIO.input(ojo)
           if i==0:
                print("NO TE VEO¡¡¡¡")
                encender(sens1,0.2) 
                clear_output(wait=True)

           else:
                print("TE VEO MACABEO¡¡¡¡")
                encender(sens2,6)
                sleep(2)
                clear_output(wait=True)
           sleep(0.2)
      except KeyboardInterrupt:
                GPIO.output(timbre,GPIO.LOW)
                GPIO.output(rojo,GPIO.LOW)
                GPIO.output(amarillo,GPIO.LOW)
                GPIO.output(azul,GPIO.LOW)
                GPIO.output(verde,GPIO.LOW)
                print("AHORA ESTOY APAGADO")
                break
    