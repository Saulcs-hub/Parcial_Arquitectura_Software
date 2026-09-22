from abc import ABC, abstractmethod
class IObservadorTarea(ABC):
    @abstractmethod
    def actualizar(self,tarea): pass
class LiderProyecto(IObservadorTarea):
    def __init__(self,nombre): self.nombre=nombre
    def actualizar(self,tarea): print(f"[OBSERVER] Líder {self.nombre}: la tarea '{tarea.nombre}' fue completada.")
class Cliente(IObservadorTarea):
    def __init__(self,nombre): self.nombre=nombre
    def actualizar(self,tarea): print(f"[OBSERVER] Cliente {self.nombre}: la tarea '{tarea.nombre}' fue completada.")
