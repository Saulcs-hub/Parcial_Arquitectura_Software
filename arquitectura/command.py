from abc import ABC, abstractmethod
from datetime import date
class OrdenCambio(ABC):
    @abstractmethod
    def ejecutar(self): pass
    @abstractmethod
    def deshacer(self): pass
    @abstractmethod
    def get_descripcion(self): pass
class AgregarRequerimiento(OrdenCambio):
    def __init__(self,proyecto,requerimiento): self.proyecto=proyecto; self.requerimiento=requerimiento
    def ejecutar(self): self.proyecto.agregar_requerimiento(self.requerimiento); print(f'[COMMAND] Agregado: {self.requerimiento}')
    def deshacer(self): self.proyecto.quitar_requerimiento(self.requerimiento); print(f'[UNDO] Eliminado: {self.requerimiento}')
    def get_descripcion(self): return f'Agregar {self.requerimiento}'
class ModificarRequerimiento(OrdenCambio):
    def __init__(self,proyecto,anterior,nuevo): self.proyecto=proyecto; self.anterior=anterior; self.nuevo=nuevo
    def ejecutar(self): self.proyecto.quitar_requerimiento(self.anterior); self.proyecto.agregar_requerimiento(self.nuevo); print(f"[COMMAND] '{self.anterior}' -> '{self.nuevo}'")
    def deshacer(self): self.proyecto.quitar_requerimiento(self.nuevo); self.proyecto.agregar_requerimiento(self.anterior); print('[UNDO] Cambio revertido.')
    def get_descripcion(self): return 'Modificar requerimiento'
class ActaReunion:
    def __init__(self,id,fecha,participantes,notas): self.id=id; self.fecha=fecha; self.participantes=participantes; self.notas=notas; self.cambios=[]
    def agregar_cambio(self,cambio): self.cambios.append(cambio)
