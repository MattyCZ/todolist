from json import dumps


class Task():
    lastID = 0

    @classmethod
    def getID(cls):
        ret = cls.lastID
        cls.lastID += 1
        return ret

    def __init__(self, label, completed=False):
        self.label = label
        self.completed = completed
        self.ID = Task.getID()

    def toDict(self):
        return {'id': self.ID, 'label': self.label, 'completed': self.completed}
