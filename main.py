from json import loads

from flask import Flask, request, jsonify
from flask_api import status

from task import Task

app = Flask('todoList')
taskList = {}


@app.route('/tasks', methods=['GET'])
def tasks():
    return jsonify({'tasks': [task.toDict() for task in taskList.values()]}), status.HTTP_200_OK


@app.route('/tasks', methods=['POST'])
def newTask():
    data = loads(request.data)
    parentTaskID = data['parentTaskID'] if 'parentTaskID' in data.keys() else None
    task = Task(data['label'])

    # saving as string might be less memory efficient but avoids mistakes from conversion
    # could be fixed by class, that has some interface, that automatically converts to ints
    taskList[str(task.ID)] = task
    if parentTaskID:
        parentTask = taskList[parentTaskID]
        if parentTask == task:
            del taskList[str(task.ID)]
            return jsonify({'error': 'Parent task cannot be itself'}), status.HTTP_400_BAD_REQUEST
        task.parent = parentTask
        parentTask.addSubTask(task)
    return jsonify({'task': task.toDict()}), status.HTTP_201_CREATED


@app.route('/tasks/<ID>', methods=['PUT'])
def updateTask(ID):
    if ID not in taskList.keys():
        return jsonify({'error': 'Task was not found'}), status.HTTP_404_NOT_FOUND
    task = taskList[ID]
    data = loads(request.data)

    # this could be optimized to not change if the parent task is the same
    # also this could/should be extracted into its own function, longer than one screen
    if 'parentTaskID' in data.keys():
        parentTaskID = data.pop('parentTaskID')
        if parentTaskID == ID:
            return jsonify({'error': 'Parent task cannot be itself'}), status.HTTP_400_BAD_REQUEST
        elif parentTaskID not in taskList.keys():
            return jsonify({'error': 'Parent task not found'}), status.HTTP_404_NOT_FOUND
        elif parentTaskID:
            # If parent task is not none -> we want to change it to different one, so it must exist
            parentTask = taskList[parentTaskID]
            parentTask.addSubTask(task)
        else:
            # If we want to change the task from sub task to non sub task
            parentTask = None

        task.parent.deleteSubTask(ID)
        task.parent = parentTask

    if 'completed' in data.keys():
        task.completed = data.pop('completed')
    if 'label' in data.keys():
        task.label = data.pop('label')

    return jsonify({'task': task.toDict()}), status.HTTP_200_OK


@app.route('/tasks/<ID>', methods=['DELETE'])
def deleteTask(ID):
    if ID not in taskList.keys():
        return jsonify({'error': 'Task was not found'}), status.HTTP_404_NOT_FOUND

    # To me it makes sense, that if task gets deleted, all sub-tasks goes with it
    # So lets recursively flatten the possibly infinite sub-task list
    for subTask in taskList[ID].flattenSubTasks():
        del taskList[str(subTask.ID)]
    del taskList[ID]
    return jsonify({}), status.HTTP_204_NO_CONTENT


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
