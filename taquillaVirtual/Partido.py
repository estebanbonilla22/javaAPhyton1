class Partido:
    def __init__(self, equipo_local, equipo_visitante, fecha):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"
