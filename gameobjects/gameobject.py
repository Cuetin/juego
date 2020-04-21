class GameObject:
    class_name = ""
    description = ""
    ps = 0
    state = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.name] = self

    def get_description(self):
        return "Raza: " + self.class_name + "\n" + self.description + "\nHP: " + str(self.ps) + "\nEstado: " + self.state

