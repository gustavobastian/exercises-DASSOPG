class Corcho:
    _bodega=""
    def __init__(self,bodega) :
        self._bodega=bodega

    def set_bodega(self,bodega):
        self._bodega=bodega

    def get_bodega(self):
        return self._bodega

class Botella:
    _corchoLocal= Corcho("None")
    def __init__(self) :
        self._corchoLocal=Corcho("None")

    def set_corchoLocal(self,corchoLocal):
        self._corchoLocal=corchoLocal  

    def get_corchoLocal(self):
        return self._corchoLocal

class Sacacorchos:
    _corchoSacado= Corcho("None")
    def __init__(self) :
        self.corchoSacado= Corcho("None")

    def get_corchoName(self):
        return self._corchoSacado.get_bodega()

    def destapar(self,botella):
        if(botella.get_corchoLocal()=="None"): raise Exception("Botella ya destapada")
        if(self.get_corchoName()!="None"): raise Exception("Sacacorchos ocupado")
        self._corchoSacado=botella.get_corchoLocal()
        botella.set_corchoLocal("None")

    def limpiar(self):
        if self.get_corchoName()=="None": raise Exception("sin corcho")
        self._corchoSacado=Corcho("None")

