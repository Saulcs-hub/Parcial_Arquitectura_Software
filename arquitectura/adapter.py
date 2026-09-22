from abc import ABC, abstractmethod
class GoogleCalendarAPI:
    def crear_evento_google(self,titulo,fecha,invitados): print(f"[GOOGLE API] Evento '{titulo}' creado."); return True
class OutlookCalendarAPI:
    def crear_cita_outlook(self,asunto,dia,contactos): print(f"[OUTLOOK API] Cita '{asunto}' creada."); return True
class ServicioCalendario(ABC):
    @abstractmethod
    def agendar_reunion(self,titulo,fecha,participantes): pass
class GoogleCalendarAdapter(ServicioCalendario):
    def __init__(self,google_api): self.google_api=google_api
    def agendar_reunion(self,titulo,fecha,participantes): return self.google_api.crear_evento_google(titulo,fecha,participantes)
class OutlookCalendarAdapter(ServicioCalendario):
    def __init__(self,outlook_api): self.outlook_api=outlook_api
    def agendar_reunion(self,titulo,fecha,participantes): return self.outlook_api.crear_cita_outlook(titulo,fecha,participantes)
