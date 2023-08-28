class Control:

    def enlazar (self, tv):
        self._tv = tv
        self._tv.setControl(self)
        
    def turnOn (self):
        if self._tv == False:
            return self._tv.turnOn()
            
    def turnOff (self):
        if self._tv == True:
            return self._tv.turnOff()

    def getEstado (self):
        return self._estado
    
    def canalUp (self):
        if self._tv == True and self._canal < 120:
            self._canal += 1
        
    def canalDown (self):
        if self._tv == True and self._canal > 0:
            self._canal -= 1

    def volumenUp (self):
        if self._tv == True and self._volumen < 7:
            self._volumen += 1
        
    def volumenDown (self):
        if self._tv == True and self._volumen > 0:
            self._volumen -= 1
    
    def setCanal (self, canal):
        self._canal = canal
    
    def setVolumen (self, volumen):
        self._volumen = volumen
        
    def getTv (self):
        return self._tv
    
    def setTv (self, tv):
        self._tv = tv
