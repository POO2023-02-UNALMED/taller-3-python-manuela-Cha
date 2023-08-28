class Control:
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
        self._tv = tv
        self._tv.setControl(self)
        
    def getTv (self):
        return self._tv
    
    def setTv (self, tv):
        self._tv = tv
