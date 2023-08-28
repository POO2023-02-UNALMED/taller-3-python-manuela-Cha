class Control:

    def enlazar (self, tv):
        self._tv = tv
        self._tv.setControl(self)
        
    def turnOn (self):
        if self._tv != None:
            return self._tv.turnOn()
            
    def turnOff (self):
        if self._tv != None:
            return self._tv.turnOff()

    def getEstado (self):
        return self._estado
    
    def canalUp (self):
        if self._tv != None:
            return self._tv.canalUp()
        
    def canalDown (self):
        if self._tv != None:
            return self._tv.canalDown()

    def volumenUp (self):
        if self._tv != None:
            return self._tv.volumenUp()
        
    def volumenDown (self):
        if self._tv != None:
            return self._tv.volumenDown()
    
    def setCanal (self, canal):
        self._canal = canal
    
    def setVolumen (self, volumen):
        self._volumen = volumen
        
    def getTv (self):
        return self._tv
    
    def setTv (self, tv):
        self._tv = tv
