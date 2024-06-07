from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId  # Import ObjectId from bson

app = Flask(__name__)

# Configuration
app.config['MONGO_URI'] = "mongodb://mongodb:27017/todo_db"

# Initialize MongoDB client
client = MongoClient(app.config['MONGO_URI'])
db = client.todo_db
todos = db.todos

@app.route('/')
def index():
    all_todos = list(todos.find())
    return render_template('index.html', todos=all_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_item = request.form.get('todo')
    if todo_item:
        todos.insert_one({'task': todo_item, 'done': False})
    return redirect(url_for('index'))

@app.route('/delete/<todo_id>', methods=['POST'])
def delete_todo(todo_id):
    todos.delete_one({'_id': ObjectId(todo_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
