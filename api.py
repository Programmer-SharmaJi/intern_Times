from flask import Flask, request, jsonify
from logger import Logger

app = Flask(__name__)
logger = Logger()

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    message = data['message']
    severity = data.get('severity', 'INFO')
    metadata = data.get('metadata', None)
    logger.log(message, severity, metadata)
    return jsonify({'status': 'success'})

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = []
    current = logger.log_list.head.next
    while current != logger.log_list.head:
        log_entry = {
            'timestamp': current.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'severity': current.severity,
            'message': current.message,
            'metadata': current.metadata
        }
        logs.append(log_entry)
        current = current.next
    log_entry = {
        'timestamp': logger.log_list.head.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'severity': logger.log_list.head.severity,
        'message': logger.log_list.head.message,
        'metadata': logger.log_list.head.metadata
    }
    logs.append(log_entry)
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
