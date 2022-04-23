class Ventana:
    __titulo = ""
    __xSuperiorIzquierdo = 10
    __ySuperiorIzquierdo = 10
    __xInferiorDerecho = 100
    __yInferiorDerecho = 100

    def __init__(self, titulo, xSuperiorIzquierdo=10, ySuperiorIzquierdo=10, xInferiorDerecho=100, yInferiorDerecho=100):
        self.__titulo = titulo
        self.__xSuperiorIzquierdo = xSuperiorIzquierdo
        self.__ySuperiorIzquierdo = ySuperiorIzquierdo
        self.__xInferiorDerecho = xInferiorDerecho
        self.__yInferiorDerecho = yInferiorDerecho
    
    def getTitulo(self):
        return self.__titulo


    def alto(self):
        return self.__yInferiorDerecho - self.__ySuperiorIzquierdo

    def ancho(self):
        return self.__xInferiorDerecho - self.__xSuperiorIzquierdo

    def mostrar(self):
        print ("Titulo: {0}\nCoordenadas de limite superior izquierdo: X = {1}  Y = {2}\nCoordenadas de limite inferior derecho: X = {3}  Y ={4}".format(self.getTitulo(), self.__xSuperiorIzquierdo, self.__ySuperiorIzquierdo, self.__xInferiorDerecho, self.__yInferiorDerecho))
    
    def moverDerecha(self, desplazamiento=5):
        if self.__xInferiorDerecho + desplazamiento <= 500:
            self.__xSuperiorIzquierdo += desplazamiento
            self.__xInferiorDerecho += desplazamiento
        else:
            print("[ERROR] El desplazamiento es demasiado grande")
    
    def moverIzquierda(self, desplazamiento=5):
        if self.__xSuperiorIzquierdo - desplazamiento >= 0:
            self.__xSuperiorIzquierdo -= desplazamiento
            self.__xInferiorDerecho -= desplazamiento
        else:
            print("[ERROR] El depsplazamiento es demasiado grande")
    
    def bajar(self, desplazamiento=5):
        if self.__yInferiorDerecho + desplazamiento <= 500:
            self.__ySuperiorIzquierdo += desplazamiento
            self.__yInferiorDerecho += desplazamiento
        else:
            print("[ERROR] El desplazamiento es demasiado grande")

    def subir(self, desplazamiento=5):
        if self.__ySuperiorIzquierdo - desplazamiento >= 0:
            self.__ySuperiorIzquierdo -= desplazamiento
            self.__yInferiorDerecho -= desplazamiento
        else:
            print("[ERROR] El desplazamieno es demasiado grande")