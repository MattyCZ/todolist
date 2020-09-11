from json import loads

from flask import Flask, request, jsonify
from flask_api import status

from task import Task

app = Flask('todoList')
taskList = {}


@app.route('/tasks', methods=['GET'])
def tasks():
    return jsonify({'tasks': [taskList[task].toDict() for task in taskList]}), status.HTTP_200_OK


@app.route('/tasks', methods=['POST'])
def newTask():
    data = loads(request.data)
    if 'label' not in data or len(data.keys()) != 1:
        return jsonify({'message': 'Not like this'}), status.HTTP_400_BAD_REQUEST
    task = Task(data['label'])
    taskList[str(task.ID)] = task  # saving as string might be less efficient but avoids mistakes from conversion
    return jsonify({'task': task.toDict()}), status.HTTP_201_CREATED


@app.route('/tasks/<ID>', methods=['POST'])
def updateTask(ID):
    if ID not in taskList.keys():
        return jsonify({'error': 'Task was not found'}), status.HTTP_404_NOT_FOUND
    task = taskList[ID]
    data = loads(request.data)
    if 'completed' in data.keys():
        task.completed = data.pop('completed')
    if 'label' in data.keys():
        task.label = data.pop('label')
    return jsonify({'task': task.toDict()}), status.HTTP_200_OK


@app.route('/tasks/<ID>', methods=['DELETE'])
def deleteTask(ID):
    if ID not in taskList.keys():
        return jsonify({'error': 'Task was not found'}), status.HTTP_404_NOT_FOUND
    del taskList[ID]
    return jsonify({}), status.HTTP_204_NO_CONTENT


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
