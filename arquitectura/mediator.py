class BitacoraReuniones:
    def __init__(self): self.actas=[]
    def guardar_acta(self,acta): self.actas.append(acta); print(f'[BITÁCORA] Acta {acta.id} guardada.')
class CronogramaProyecto:
    def actualizar_con_cambios(self): print('[CRONOGRAMA] Cronograma actualizado.')
class Notificador:
    def notificar(self,destinatario,mensaje): print(f'[NOTIFICACIÓN] {destinatario}: {mensaje}')
class MediadorProyecto:
    def __init__(self,bitacora,cronograma,notificador): self.bitacora=bitacora; self.cronograma=cronograma; self.notificador=notificador
    def registrar_acta(self,acta):
        print('\n[MEDIATOR] Procesando acta...'); self.bitacora.guardar_acta(acta)
        for cambio in acta.cambios: cambio.ejecutar()
        self.cronograma.actualizar_con_cambios(); self.notificador.notificar('Desarrolladores','El proyecto tiene nuevos cambios.')
