class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
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

    @classmethod
    def getNumTV (cls):
        return cls._numTV 
    
    @classmethod
    def setNumTV (cls):
        cls._numTV = _numTV
