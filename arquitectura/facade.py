from .config import ConfiguracionSistema
from .testing import PipelinePruebas,FabricaWeb,FabricaMobile,FabricaCloud
from .mediator import BitacoraReuniones,CronogramaProyecto,Notificador,MediadorProyecto
from .modelos import Proyecto
class SistemaGestionFacade:
    def __init__(self): self.proyectos=[]; self.empleados=[]; self.configuracion=ConfiguracionSistema(); self.pipeline=PipelinePruebas(); self.mediador=MediadorProyecto(BitacoraReuniones(),CronogramaProyecto(),Notificador())
    def crear_proyecto(self,nombre,tecnologia='WEB'):
        proyecto=Proyecto(str(len(self.proyectos)+1),nombre,'Proyecto DevEnterprise',tecnologia); self.proyectos.append(proyecto); print(f"[FACADE] Proyecto '{nombre}' creado."); return proyecto
    def asignar_empleado(self,proyecto,empleado):
        if empleado.puede_asignarse(): empleado.cambiar_estado(__import__('arquitectura.state',fromlist=['AsignadoProyecto']).AsignadoProyecto()); print(f'[FACADE] {empleado.nombre} asignado a {proyecto.nombre}.')
        else: print('[FACADE] El empleado no está disponible.')
    def ejecutar_pipeline_pruebas(self,proyecto):
        fabrica={'WEB':FabricaWeb,'MOBILE':FabricaMobile}.get(proyecto.tecnologia.upper(),FabricaCloud)(); return self.pipeline.ejecutar(fabrica.crear_paquete(proyecto))
    def registrar_acta_reunion(self,acta): self.mediador.registrar_acta(acta)
    def agendar_reunion(self,titulo,fecha):
        calendario=self.configuracion.get_servicio_calendario()
        if calendario is None: print('No existe servicio de calendario configurado.'); return False
        return calendario.agendar_reunion(titulo,fecha,['cliente@empresa.com'])
