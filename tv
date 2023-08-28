class Marca:
    def __init__(self, nombre):
        self._nombre = nombre
    
    def setNombre (self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre
    
class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = Marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = Control
        TV._numTV += 1


    def setMarca (self, marca):
        self._marca = marca
    
    def getMarca (self):
        return self._marca

    def getCanal (self):
        return self._canal

    def setPrecio (self, precio):
        self._precio = precio

    def getPrecio (self):
        return self._precio
    
    def getVolumen (self):
        return self._volumen
    
    def setControl (self, control):
        self._control = control
    
    def getControl (self):
        return self._control
    
    
class Control:
    def __init__(self, tv):
        self._tv = TV

    def turnOn (self):
        self._estado = True

    def turnOff (self):
        self._estado = False

    def getEstado (self):
        return self._estado
    
    def canalUp (self):
        if self._estado == True and self._canal < 120:
            self._canal += 1
        
    def canalDown (self):
        if self._estado == True and self._canal > 1:
            self._canal -= 1

    def volumenUp (self):
        if self._estado == True and self._volumen < 7:
            self._canal += 1
        
    def volumenDown (self):
        if self._estado == True and self._canal > 0:
            self._canal -= 1
    
    def setCanal (self, canal):
        self._canal = canal
    
    def setVolumen (self, volumen):
        self._volumen = volumen
    
    def enlazar (self, tv):
        self._tv = TV
        self._tv.control = self
        
    def getTv (self):
        return self._tv
    
    def setTV (self, tv):
        self._tv = tv
