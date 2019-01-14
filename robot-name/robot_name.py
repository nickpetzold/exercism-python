import weakref

class Robot(object):
    instances = []
    def __init__(self):
        self.__class__.instances.append(weakref.proxy(self))

        self.name = name

    def generate_name:
        prefix = random.sample(list(range(A-Z)), k = 2)
        suffix =
