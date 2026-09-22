from enum import Enum
from abc import ABC, abstractmethod

class EstadoTarea(Enum):
    PENDIENTE='PENDIENTE'; EN_PROGRESO='EN_PROGRESO'; COMPLETADO='COMPLETADO'; BLOQUEADO='BLOQUEADO'
class EstadoProyecto(Enum):
    PLANIFICACION='PLANIFICACION'; EN_EJECUCION='EN_EJECUCION'; COMPLETADO='COMPLETADO'; CANCELADO='CANCELADO'
class EstadoPipeline(Enum):
    PENDIENTE='PENDIENTE'; EN_EJECUCION='EN_EJECUCION'; FALLIDO='FALLIDO'; COMPLETADO='COMPLETADO'
class RolBase(Enum):
    DESARROLLADOR='DESARROLLADOR'; QA='QA'; LIDER_PROYECTO='LIDER_PROYECTO'

class IEstimable(ABC):
    @abstractmethod
    def calcular_costo(self): pass
    @abstractmethod
    def calcular_tiempo(self): pass

class SubTarea(IEstimable):
    def __init__(self,id,nombre,costo,tiempo): self.id=id; self.nombre=nombre; self.estado=EstadoTarea.PENDIENTE; self.costo=costo; self.tiempo=tiempo
    def cambiar_estado(self,estado): self.estado=estado
    def calcular_costo(self): return self.costo
    def calcular_tiempo(self): return self.tiempo

class Tarea(IEstimable):
    def __init__(self,id,nombre,descripcion): self.id=id; self.nombre=nombre; self.descripcion=descripcion; self.estado=EstadoTarea.PENDIENTE; self.subtareas=[]; self.observadores=[]
    def agregar_subtarea(self,subtarea): self.subtareas.append(subtarea)
    def agregar_observador(self,observador): self.observadores.append(observador)
    def notificar_observadores(self):
        for observador in self.observadores: observador.actualizar(self)
    def cambiar_estado(self,estado):
        self.estado=estado; print(f"Tarea '{self.nombre}' cambió a {estado.value}")
        if estado==EstadoTarea.COMPLETADO: self.notificar_observadores()
    def calcular_costo(self): return sum(x.calcular_costo() for x in self.subtareas)
    def calcular_tiempo(self): return sum(x.calcular_tiempo() for x in self.subtareas)

class Fase(IEstimable):
    def __init__(self,id,nombre,descripcion): self.id=id; self.nombre=nombre; self.descripcion=descripcion; self.tareas=[]
    def agregar_tarea(self,tarea): self.tareas.append(tarea)
    def calcular_costo(self): return sum(x.calcular_costo() for x in self.tareas)
    def calcular_tiempo(self): return sum(x.calcular_tiempo() for x in self.tareas)

class Proyecto(IEstimable):
    def __init__(self,id,nombre,descripcion,tecnologia='WEB'):
        self.id=id; self.nombre=nombre; self.descripcion=descripcion; self.tecnologia=tecnologia; self.estado=EstadoProyecto.PLANIFICACION; self.fases=[]; self.requerimientos=[]; self.metodologia=None
    def agregar_fase(self,fase): self.fases.append(fase)
    def cambiar_metodologia(self,metodologia): self.metodologia=metodologia; print('[STRATEGY] Metodología de estimación cambiada.')
    def calcular_costo(self): return self.metodologia.calcular_costo(self) if self.metodologia else sum(x.calcular_costo() for x in self.fases)
    def calcular_tiempo(self): return self.metodologia.calcular_tiempo(self) if self.metodologia else sum(x.calcular_tiempo() for x in self.fases)
    def agregar_requerimiento(self,requerimiento): self.requerimientos.append(requerimiento)
    def quitar_requerimiento(self,requerimiento):
        if requerimiento in self.requerimientos: self.requerimientos.remove(requerimiento)
