# Dev Enterprise OS — Patrones de diseño

Ejemplo académico en Python que modela la gestión de proyectos de software mediante patrones GoF. El programa conserva la demostración original, pero el código está separado por responsabilidades para facilitar su lectura y mantenimiento.

## Arquitectura

```text
main.py
└── arquitectura/
    ├── modelos.py       # Entidades y Composite: Proyecto/Fase/Tarea/SubTarea
    ├── observer.py      # Avisos al líder y al cliente al completar tareas
    ├── strategy.py      # Estimación por horas o puntos de función
    ├── decorator.py     # Responsabilidades dinámicas de empleados
    ├── state.py         # Estados de disponibilidad del empleado
    ├── testing.py       # Factory Method y Chain of Responsibility
    ├── command.py       # Cambios de requerimientos y Undo
    ├── mediator.py      # Actas, cronograma y notificaciones
    ├── adapter.py       # Adaptadores de Google Calendar y Outlook
    ├── config.py        # Singleton de configuración global
    └── facade.py        # Fachada de alto nivel del sistema
```

## Patrones usados

- **Composite:** permite calcular costo y tiempo recorriendo Proyecto → Fase → Tarea → SubTarea.
- **Strategy:** cambia en ejecución entre estimación por horas y por puntos de función.
- **Observer:** notifica automáticamente a `LiderProyecto` y `Cliente` cuando una tarea pasa a completada.
- **Decorator:** encadena responsabilidades como Líder Técnico y Mentor, modificando salario y permisos.
- **State:** encapsula si un empleado está disponible, asignado o en licencia.
- **Factory Method:** crea paquetes de pruebas Web, Mobile o Cloud.
- **Chain of Responsibility:** ejecuta el pipeline de análisis estático, pruebas unitarias, integración y seguridad.
- **Command:** encapsula cambios de requerimientos y permite deshacerlos.
- **Mediator:** coordina bitácora, cronograma y notificaciones al registrar un acta.
- **Adapter:** ofrece una interfaz común para APIs de calendarios distintas.
- **Singleton:** garantiza una única configuración del sistema.
- **Facade:** simplifica la creación de proyectos, asignaciones, pipeline, actas y reuniones.

## Ejecución

Requiere Python 3.9 o posterior. Desde esta carpeta ejecuta:

```bash
python main.py
```

La salida demuestra el flujo completo: cambio de estrategia de estimación, notificaciones Observer, responsabilidades Decorator, cambio de estado, pipeline de pruebas, Command/Undo, Mediator y Adapter.

## Punto de entrada

`main.py` contiene únicamente la composición del ejemplo y la función `demo()`. Las implementaciones reutilizables viven dentro del paquete `arquitectura`, por lo que pueden importarse en futuras pruebas o aplicaciones sin copiar el programa completo.

Autores: Carlos Saul Villabona Pinilla y Edwar Alejandro Jimenez Rios
