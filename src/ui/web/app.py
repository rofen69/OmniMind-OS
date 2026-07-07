import logging
from flask import Flask, request, jsonify, render_template

from src.core.orchestrator import Orchestrator
from src.core.planner import Planner
from src.core.registry import AgentRegistry

app = Flask(__name__)

# Real-time Logging Handler
log_stream = []

class ListHandler(logging.Handler):
    def emit(self, record):
        # We append simple text to a list, UI will pull it
        log_msg = self.format(record)
        log_stream.append(log_msg)

handler = ListHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
# Attach to root logger so we get logs from core, agents, discovery, etc.
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(handler)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/execute', methods=['POST'])
def execute_task():
    data = request.json
    task = data.get('task', '')
    
    if not task:
        return jsonify({"error": "No task provided"}), 400
        
    # Clear previous logs for this new execution trace
    log_stream.clear()
    
    planner = Planner()
    registry = AgentRegistry()
    orchestrator = Orchestrator(planner, registry)
    
    # We pass no callback because the web UI defaults to 'Auto-Execute'
    result = orchestrator.run(task)
    
    return jsonify(result)


@app.route('/api/logs', methods=['GET'])
def get_logs():
    # Return all logs captured so far, frontend will render them
    return jsonify({"logs": list(log_stream)})


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
