from flask import Flask, jsonify, request

app = Flask(__name__)

# Data structure to store todos in memory (server restart par data delete ho jayega)
todos = [
    {"id": 1, "task": "Task 1: Complete Docker Deployment"},
    {"id": 2, "task": "Task 2: Setup CI/CD Pipeline"}
]
next_id = 3

@app.route('/')
def hello_cloud():
    return 'Hello from KooLabs! (Todo Service)'

# Health Check route
@app.route('/healthz')
def health_check():
    return jsonify({'status': 'ok'}), 200

# GET: Sabhi todos dikhana
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST: Naya todo item add karna
@app.route('/api/todos', methods=['POST'])
def add_todo():
    global next_id
    if not request.json or not 'task' in request.json:
        return jsonify({'error': 'Task is required'}), 400
    
    new_todo = {
        'id': next_id,
        'task': request.json['task']
    }
    todos.append(new_todo)
    next_id += 1
    return jsonify(new_todo), 201

if __name__ == '__main__':
    # Gunicorn ya production server isay handle karega
    app.run(host='0.0.0.0', port=5000)