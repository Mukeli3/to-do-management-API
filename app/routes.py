#!/usr/bin/python3
from app.model import ToDo
from flask import Blueprint, request, jsonify
from app import db

todo = Blueprint('todo', __name__)

@todo.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title:
        return jsonify({"error": "Title is required"}), 400

    new = ToDo(title=title, description=description)
    db.session.add(new)
    db.session.commit()

    return jsonify({"message": "To-do created successfully", "id": new.id}), 200

# list all to-dos
@todo.route('/todos', methods=['GET'])
def get_todos():
    todos = ToDo.query.all() # fetch all records from ToDo
    return jsonify([
        {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'status': todo.status,
            'created_at': todo.created_at,
            'updated_at':todo.updated_at
        }
        for todo in todos
    ])

# get a specific to-do with id
@todo.route('/todos/<int:todo_id>', methods=['GET'])
def get_single_todo(todo_id):
    todo = ToDo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "To-do not found"}), 404

    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'status': todo.status,
        'created_at': todo.created_at,
        'updated_at': todo.updated_at
    })

#update a to-do
@todo.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = ToDo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "To-do item not found"}), 404

    data = request.get_json()
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.status = data.get('status', todo.status)

    db.session.commit()
    return jsonify({"message": "To-do succefully updated"})

# delete a to-do item
@todo.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = ToDo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "To-do not found"}), 404

    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "To-do successfully deleted"})