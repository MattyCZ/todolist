# TODO list API

1. Please create a server application with the API documented below
    - Feel free to use a web framework of your choice in Python - Django is prefferred, but a micro-framework such as Flask is also a good choice
    - Try to write a clean and well designed code for me to inspect
    - Specify a guide to run the server app in README 
    - The Server App doesn't need to have a persistent data storage, you can just store the data in-memory or whatever you prefer

2. Design an API change to make it possible to create a nested list of subtasks for every task (even for subtasks)
    - update the documentation below and add it to the project source as `api-doc.md`
    - also update the application to support subtasks

- Contact me at tom@avocode.com if there you have any question

# API Documentation

## Endpoints:

### `GET /tasks`

Returns a list of tasks.

```
> GET /tasks

< 200 OK
{
  tasks: Task[] = [
    { id: number, label: string, completed: boolean }
  ]
}
```

### `POST /tasks`

Creates a new task.

```
> POST /tasks
{ label: string }

< 201 Created
{
  task: { id: number, label: string, completed: boolean }
}
```

### `POST /tasks/:id`

Updates the task of the given ID.

```
> POST /tasks/:id
{ label: string } |
{ completed: boolean } |
{ label: string, completed: boolean }

< 200 OK
{
  task: Task = { id: number, label: string, completed: boolean }
}

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