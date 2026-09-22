class ConfiguracionSistema:
    _instancia=None
    def __new__(cls):
        if cls._instancia is None: cls._instancia=super().__new__(cls); cls._instancia.propiedades={}; cls._instancia.servicio_calendario=None
        return cls._instancia
    def configurar(self,propiedad,valor): self.propiedades[propiedad]=valor
    def obtener(self,propiedad): return self.propiedades.get(propiedad)
    def set_servicio_calendario(self,servicio): self.servicio_calendario=servicio
    def get_servicio_calendario(self): return self.servicio_calendario
