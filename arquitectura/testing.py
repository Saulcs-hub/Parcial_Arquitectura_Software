from abc import ABC, abstractmethod
from .modelos import EstadoPipeline
class PaquetePrueba(ABC):
    def __init__(self,id,tecnologia): self.id=id; self.tecnologia=tecnologia; self.fallar_en=None
    def obtener_detalles(self): return f'Paquete {self.id} - {self.tecnologia}'
    @abstractmethod
    def validar_entorno(self): pass
class PaquetePruebaWeb(PaquetePrueba):
    def validar_entorno(self): print('[WEB] Validando navegador y compatibilidad.'); return True
class PaquetePruebaMobile(PaquetePrueba):
    def validar_entorno(self): print('[MOBILE] Validando dispositivo y sistema operativo.'); return True
class PaquetePruebaCloud(PaquetePrueba):
    def validar_entorno(self): print('[CLOUD] Validando proveedor y región.'); return True
class FabricaPaquetePrueba(ABC):
    @abstractmethod
    def crear_paquete(self,proyecto): pass
class FabricaWeb(FabricaPaquetePrueba):
    def crear_paquete(self,proyecto): print('[FACTORY] Creando paquete WEB.'); return PaquetePruebaWeb(f'WEB-{proyecto.id}','WEB')
class FabricaMobile(FabricaPaquetePrueba):
    def crear_paquete(self,proyecto): print('[FACTORY] Creando paquete MOBILE.'); return PaquetePruebaMobile(f'MOBILE-{proyecto.id}','MOBILE')
class FabricaCloud(FabricaPaquetePrueba):
    def crear_paquete(self,proyecto): print('[FACTORY] Creando paquete CLOUD.'); return PaquetePruebaCloud(f'CLOUD-{proyecto.id}','CLOUD')
class PasoPrueba(ABC):
    def __init__(self,nombre): self.nombre=nombre; self.siguiente=None
    def set_siguiente(self,siguiente): self.siguiente=siguiente; return siguiente
    def ejecutar(self,paquete):
        print(f'Ejecutando: {self.nombre}')
        if not self.validar(paquete): print(f'[FALLO] {self.nombre}. Pipeline detenido.'); return False
        print(f'[OK] {self.nombre} aprobada.'); return self.siguiente.ejecutar(paquete) if self.siguiente else True
    @abstractmethod
    def validar(self,paquete): pass
class AnalisisEstatico(PasoPrueba):
    def __init__(self): super().__init__('Análisis Estático')
    def validar(self,paquete): return paquete.fallar_en!='ANALISIS'
class PruebasUnitarias(PasoPrueba):
    def __init__(self): super().__init__('Pruebas Unitarias')
    def validar(self,paquete): return paquete.fallar_en!='UNITARIAS'
class PruebasIntegracion(PasoPrueba):
    def __init__(self): super().__init__('Pruebas de Integración')
    def validar(self,paquete): return paquete.fallar_en!='INTEGRACION'
class PruebasSeguridad(PasoPrueba):
    def __init__(self): super().__init__('Pruebas de Seguridad')
    def validar(self,paquete): return paquete.fallar_en!='SEGURIDAD'
class PipelinePruebas:
    def __init__(self):
        self.estado=EstadoPipeline.PENDIENTE; self.analisis=AnalisisEstatico(); self.unitarias=PruebasUnitarias(); self.integracion=PruebasIntegracion(); self.seguridad=PruebasSeguridad(); self.analisis.set_siguiente(self.unitarias).set_siguiente(self.integracion).set_siguiente(self.seguridad)
    def ejecutar(self,paquete):
        self.estado=EstadoPipeline.EN_EJECUCION; print('\n--- PIPELINE DE PRUEBAS ---')
        if not paquete.validar_entorno(): self.estado=EstadoPipeline.FALLIDO; return False
        resultado=self.analisis.ejecutar(paquete); self.estado=EstadoPipeline.COMPLETADO if resultado else EstadoPipeline.FALLIDO
        if resultado: print('[OK] Pipeline completado.')
        return resultado
