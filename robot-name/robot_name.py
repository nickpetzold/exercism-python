import random

class Robot(object):
    instances = []
    def __init__(self):
        self.set_name()
        Robot.instances.append(self.name)

    def generate_name(self):
        name = ''
        for _ in range(2):
            name += random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)[0]
        for _ in range(3):
            name += random.sample('0123456789', 1)[0]
        return name

    def reset(self):
        self.set_name()

    def set_name(self):
        name = self.generate_name()
        while name in Robot.instances:
            name = self.generate_name()
        self.name = name
