class Corcho:
    _bodega=""
    def __init__(self,bodega) :
        self._bodega=bodega

    def set_bodega(self,bodega):
        self._bodega=bodega

    def get_bodega(self):
        return self._bodega

class Botella:
    _corchoLocal= Corcho()
    def __init__(self) :
        self.corchoLocal="None"

    def set_corchoLocal(self,corchoLocal):
        self._corchoLocal=corchoLocal  

    def get_corchoLocal(self):
        return self._corchoLocal

class Sacacorchos:
    _corchoSacado= Corcho()
    def __init__(self) :
        self.corchoSacado= None

    def get_corchoName(self):
        return self._corchoName

    def destapar(self,botella):
        
        self._corchoSacado=botella.get_corchoLocal()
        botella.set_corchoLocal("None")

    def limpiar(self,botella):
        self._corchoSacado="None"

