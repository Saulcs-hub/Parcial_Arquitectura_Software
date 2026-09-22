from abc import ABC, abstractmethod
from .modelos import RolBase
from .decorator import EmpleadoBase
class EstadoEmpleado(ABC):
    @abstractmethod
    def puede_asignarse(self): pass
    @abstractmethod
    def nombre(self): pass
class EnDisponibilidad(EstadoEmpleado):
    def puede_asignarse(self): return True
    def nombre(self): return 'EN DISPONIBILIDAD'
class AsignadoProyecto(EstadoEmpleado):
    def puede_asignarse(self): return False
    def nombre(self): return 'ASIGNADO A PROYECTO'
class EnLicencia(EstadoEmpleado):
    def puede_asignarse(self): return False
    def nombre(self): return 'EN LICENCIA'
class Empleado:
    def __init__(self,id,nombre,email,rol_base,salario_base): self.id=id; self.nombre=nombre; self.email=email; self.rol_base=rol_base; self.salario_base=salario_base; self.estado=EnDisponibilidad(); self.responsabilidad=EmpleadoBase()
    def cambiar_estado(self,estado): self.estado=estado
    def puede_asignarse(self): return self.estado.puede_asignarse()
    def asignar_responsabilidad(self,responsabilidad): self.responsabilidad=responsabilidad
    def calcular_salario(self): return self.responsabilidad.modificar_salario(self.salario_base)
    def obtener_permisos(self): return self.responsabilidad.otorgar_permisos()
