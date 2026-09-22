from datetime import date
from arquitectura.modelos import EstadoTarea,RolBase,Fase,Tarea,SubTarea
from arquitectura.observer import LiderProyecto,Cliente
from arquitectura.strategy import EstimacionPorHoras,EstimacionPorPuntosFuncion
from arquitectura.decorator import LiderTecnicoDecorator,MentorDecorator
from arquitectura.state import Empleado
from arquitectura.command import AgregarRequerimiento,ActaReunion
from arquitectura.adapter import GoogleCalendarAPI,GoogleCalendarAdapter
from arquitectura.config import ConfiguracionSistema
from arquitectura.facade import SistemaGestionFacade

def demo():
    print('\n'+'='*55+'\n        DEV ENTERPRISE OS\n'+'='*55)
    sistema=SistemaGestionFacade(); ConfiguracionSistema().set_servicio_calendario(GoogleCalendarAdapter(GoogleCalendarAPI()))
    proyecto=sistema.crear_proyecto('Sistema Ecommerce','WEB')
    fase=Fase('F01','Desarrollo','Fase de desarrollo'); tarea=Tarea('T01','Crear módulo Login','Desarrollar autenticación')
    tarea.agregar_subtarea(SubTarea('ST01','Backend Login',500_000,10)); tarea.agregar_subtarea(SubTarea('ST02','Frontend Login',400_000,8)); fase.agregar_tarea(tarea); proyecto.agregar_fase(fase)
    proyecto.cambiar_metodologia(EstimacionPorHoras(50_000)); print('\nCosto por horas:',proyecto.calcular_costo())
    proyecto.cambiar_metodologia(EstimacionPorPuntosFuncion(100_000,15)); print('Costo por puntos de función:',proyecto.calcular_costo())
    tarea.agregar_observador(LiderProyecto('Carlos')); tarea.agregar_observador(Cliente('Empresa ABC')); print('\n--- OBSERVER ---'); tarea.cambiar_estado(EstadoTarea.COMPLETADO)
    print('\n--- PERSONAL ---'); empleado=Empleado('E01','Juan Pérez','juan@empresa.com',RolBase.DESARROLLADOR,3_000_000); r=LiderTecnicoDecorator(empleado.responsabilidad); empleado.asignar_responsabilidad(MentorDecorator(r)); print('Responsabilidades:',empleado.responsabilidad.get_nombre()); print('Salario:',empleado.calcular_salario()); print('Permisos:',empleado.obtener_permisos()); sistema.asignar_empleado(proyecto,empleado); print('Estado:',empleado.estado.nombre())
    print('\n--- PIPELINE ---'); sistema.ejecutar_pipeline_pruebas(proyecto)
    print('\n--- COMMAND ---'); comando=AgregarRequerimiento(proyecto,'Implementar autenticación de dos factores'); comando.ejecutar(); print('Requerimientos:',proyecto.requerimientos); comando.deshacer(); print('Después del Undo:',proyecto.requerimientos)
    print('\n--- MEDIATOR ---'); acta=ActaReunion('ACTA01',date.today(),['Cliente','Líder'],'Cambios del Sprint'); acta.agregar_cambio(AgregarRequerimiento(proyecto,'Agregar recuperación de contraseña')); sistema.registrar_acta_reunion(acta)
    print('\n--- CALENDARIO ---'); sistema.agendar_reunion('Revisión del proyecto',date.today()); print('\n'+'='*55+'\n          DEMOSTRACIÓN FINALIZADA\n'+'='*55)
if __name__=='__main__': demo()
