class GameObject:
    class_name = ""
    description = ""
    ps = 0
    state = ""
    objects = {}
    renderer = None
    attacks = []

    def __init__(self, name):
        self.name = name
        self.renderer = None
        GameObject.objects[self.name] = self

    def get_description(self):
        return "Raza: " + self.class_name + "\n" + self.description + "\nHP: " + str(self.ps) + "\nEstado: " + self.state

    def render(self, screen, position):
        if self.renderer:
            screen.blit(self.renderer, position)

class Attack:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg


