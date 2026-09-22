from abc import ABC, abstractmethod
class EstrategiaEstimacion(ABC):
    @abstractmethod
    def calcular_costo(self,proyecto): pass
    @abstractmethod
    def calcular_tiempo(self,proyecto): pass
class EstimacionPorHoras(EstrategiaEstimacion):
    def __init__(self,costo_hora): self.costo_hora=costo_hora
    def calcular_tiempo(self,proyecto): return sum(x.calcular_tiempo() for x in proyecto.fases)
    def calcular_costo(self,proyecto): return self.calcular_tiempo(proyecto)*self.costo_hora
class EstimacionPorPuntosFuncion(EstrategiaEstimacion):
    def __init__(self,costo_punto,puntos_funcion,horas_por_punto=4): self.costo_punto=costo_punto; self.puntos_funcion=puntos_funcion; self.horas_por_punto=horas_por_punto
    def calcular_costo(self,proyecto): return self.puntos_funcion*self.costo_punto
    def calcular_tiempo(self,proyecto): return self.puntos_funcion*self.horas_por_punto
