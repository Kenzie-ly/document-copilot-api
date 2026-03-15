from flask import Flask, jsonify, request

app = Flask(__name__)
model = None

def init_api(trained_model):
    global model
    model = trained_model

@app.route("/analyzerResult", methods=["GET"])
def get_analyzer_result():
    output = model.get_response()
    
    return jsonify({
        "status":"ok",
        "message" : output
    })

@app.route("/inputText", methods=["POST"]) #WHAT IF I WROTE Post
def post_input_text():
    
    data = request.get_json(force=True)
    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "Missing 'text' in request body"}), 400
  

    error_message = model.generateResponse(data["text"])
    if error_message is None: 
        return jsonify({
            "status": "ok",
            "message": "Successfully generated response."
        })
    else:
        return jsonify({
            "status": "error",
            "message": error_message
        }), 500