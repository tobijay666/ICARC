import flask

from ollama import chat
from ollama import ChatResponse

class Inference:
    def __init__(self, model_name):
        self.model = model_name

    def get_response(self, query):
        response = chat(model=self.model, messages=[
            {
                'role': 'user',
                'content': query
            },
        ])

        return response
    

class WebAPI:
    def __init__(self, host="0.0.0.0", port=5000):
        self.host = host
        self.port = port
        

    def start_server(self):
        app = flask.Flask(__name__)
        @app.route('/inference', methods=['POST'])
        def handle_inference():
            data = flask.request.get_json()
            query = data.get('query', '')
            model_name = data.get('model_name', '')
            return self.inference(query, model_name)
        app.run(host=self.host, port=self.port)

    def inference(self, query, model_name):
        inference = Inference(model_name)
        return inference.get_response(query)
    

if __name__ == "__main__":
    newServer = WebAPI()
    newServer.start_server()