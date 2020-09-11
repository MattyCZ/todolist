class Task:
    lastID = 0

    @classmethod
    def getID(cls):
        ret = cls.lastID
        cls.lastID += 1
        return ret

    def __init__(self, label: str, completed: bool = False, parent=None):
        self.label = label
        self.completed = completed
        self.ID = Task.getID()
        self.parent = parent
        self.subTasks = {}

    def toDict(self):
        return {
            'id': self.ID,
            'label': self.label,
            'completed': self.completed,
            'parent': self.parent.ID if self.parent else None,
            'subTasks': [subTask.ID for subTask in self.subTasks.values()]  # only sending ID to not repeat myself
        }

    def addSubTask(self, subTask):
        self.subTasks[str(subTask.ID)] = subTask

    def deleteSubTask(self, subTaskID):
        del self.subTasks[subTaskID]

    def flattenSubTasks(self) -> list:
        subTasks = list(self.subTasks.values())
        for subTask in subTasks:
            subTasks += subTask.flattenSubTasks()
        return subTasks

    def __repr__(self):
        return str(self.ID)
