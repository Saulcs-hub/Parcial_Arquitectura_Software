from abc import ABC, abstractmethod
class IResponsabilidad(ABC):
    @abstractmethod
    def get_nombre(self): pass
    @abstractmethod
    def modificar_salario(self,base): pass
    @abstractmethod
    def otorgar_permisos(self): pass
class EmpleadoBase(IResponsabilidad):
    def get_nombre(self): return 'Empleado base'
    def modificar_salario(self,base): return base
    def otorgar_permisos(self): return []
class ResponsabilidadDecorator(IResponsabilidad):
    def __init__(self,envuelto): self.envuelto=envuelto
    def get_nombre(self): return self.envuelto.get_nombre()
    def modificar_salario(self,base): return self.envuelto.modificar_salario(base)
    def otorgar_permisos(self): return self.envuelto.otorgar_permisos()
class LiderTecnicoDecorator(ResponsabilidadDecorator):
    def get_nombre(self): return self.envuelto.get_nombre()+' + Líder Técnico'
    def modificar_salario(self,base): return self.envuelto.modificar_salario(base)*1.15
    def otorgar_permisos(self): return self.envuelto.otorgar_permisos()+['APROBAR_CODIGO','ASIGNAR_TAREAS']
class SoporteFinSemanaDecorator(ResponsabilidadDecorator):
    def get_nombre(self): return self.envuelto.get_nombre()+' + Soporte Fin de Semana'
    def modificar_salario(self,base): return self.envuelto.modificar_salario(base)+250_000
    def otorgar_permisos(self): return self.envuelto.otorgar_permisos()+['SOPORTE_PRODUCCION']
class MentorDecorator(ResponsabilidadDecorator):
    def get_nombre(self): return self.envuelto.get_nombre()+' + Mentor'
    def modificar_salario(self,base): return self.envuelto.modificar_salario(base)*1.05
    def otorgar_permisos(self): return self.envuelto.otorgar_permisos()+['GESTIONAR_MENTORIA']
