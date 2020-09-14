# API Documentation

## Endpoints:

### `GET /tasks`

Returns a list of tasks.

```
> GET /tasks

< 200 OK
{
  tasks: Task[] = [
    { id: number, label: string, completed: boolean, parent: integer, subTasks: integer[] }
  ]
}
```

### `POST /tasks`

Creates a new task.

```
> POST /tasks
{ label: string, parentTaskID: string }

< 201 Created
{
  task: { id: number, label: string, completed: boolean, parent: integer, subTasks: integer[] }
}

< 400 Bad Request
{
  error: string
}
```

### `PUT /tasks/:id`

Updates the task of the given ID.

```
> PUT /tasks/:id
{ label: string } |
{ completed: boolean } |
{ label: string, completed: boolean } |
{ label: string, parentTaskID: string } |
{ completed: boolean, parentTaskID: string } |
{ label: string, completed: boolean, parentTaskID: string }

< 200 OK
{
  task: Task = { id: number, label: string, completed: boolean, parent: integer, subTasks: integer[] }
}

< 400 Bad Request
{ error: string }

< 404 Not Found
{ error: string }
```

### `DELETE /tasks/:id`

Deletes the task of the given ID.

```
> DELETE /tasks/:id

< 204 No Content

< 404 Not Found
{ error: string }
```