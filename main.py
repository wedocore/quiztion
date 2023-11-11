import requests
from flask import Flask, request, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
  return "Hello world!  Your web application is working!"


@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('.',
                             'ai-plugin.json',
                             mimetype='application/json')


@app.route('/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
