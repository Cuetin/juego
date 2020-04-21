from .gameobject import GameObject

class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "Duende"
        self.description = "Los duendes son criaturas mitológicas fantásticas de forma humanoide pero del tamaño de un niño pequeño.\nSuelen ir equipados con armas robadas como espadas y escudos de madera."
        self.ps = 5
        self._state = "Como un roble"
        super().__init__(name)

    @property
    def state(self):
        if self.ps >= 4:
            self._state = '"Como un roble"'
        elif self.ps >= 2:
            self._state = '"Esta jodido"'
        elif self.ps == 1:
            self._state = '"Esta para ir a la UCI"'
        elif self.ps <= 0:
            self._state = '"Esta mas muerto que muertini"'
        return self._state

    @state.setter
    def state(self, val):
        self._state = val

class Elf(GameObject):
    def __init__(self, name):
        self.class_name = "Elfo"
        self.description = "Los elfos son..."
        self.ps = 20
        self._state = "Como un roble"
        super().__init__(name)

    @property
    def state(self):
        if self.ps >= 15:
            self._state = "Como un roble"
        elif self.ps >= 10:
            self._state = '"Esta jodido"'
        elif self.ps >= 5:
            self._state = '"Esta para ir a la UCI"'
        elif self.ps <= 0:
            self._state = '"Esta mas muerto que muertini"'
        return self._state

    @state.setter
    def state(self, val):
        self._state = val