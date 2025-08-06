class MascotaU:
    def __init__(self, nombre, codigo_estudiante, evento_asignado, horas_acumuladas):
        self.nombre = nombre
        self.codigo_estudiante = codigo_estudiante
        self.evento_asignado = evento_asignado
        self.horas_acumuladas = horas_acumuladas

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_codigo_estudiante(self):
        return self.codigo_estudiante

    def set_codigo_estudiante(self, codigo_estudiante):
        self.codigo_estudiante = codigo_estudiante

    def get_evento_asignado(self):
        return self.evento_asignado

    def set_evento_asignado(self, evento_asignado):
        self.evento_asignado = evento_asignado

    def get_horas_acumuladas(self):
        return self.horas_acumuladas

    def set_horas_acumuladas(self, horas_acumuladas):
        self.horas_acumuladas = horas_acumuladas

    def registrar_horas(self, horas):
        self.horas_acumuladas += horas
        return self.horas_acumuladas

    def verificar_estado(self):
        if self.horas_acumuladas >= 8:
            return "Horas completadas"
        elif self.horas_acumuladas < 8:
            return "Horas pendientes"
        return "Estado desconocido"

    def __str__(self):
        return (f"MascotaU{{nombre='{self.nombre}', "
                f"codigoEstudiante='{self.codigo_estudiante}', "
                f"eventoAsignado='{self.evento_asignado}', "
                f"horasAcumuladas={self.horas_acumuladas}}}")
