from flask import Flask, jsonify, request

app = Flask(__name__)
model = None

def init_api(trained_model):
    global model
    model = trained_model

@app.route("/analyzeNote", methods=["POST"])
def post_analyze_Note():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "Missing 'text' in request body"}), 400

    success, result_text = model.generateResponse(data["text"])
    
    if success: 
        return jsonify({
            "status": "ok",
            "message": result_text
        })
    else:
        return jsonify({
            "status": "error",
            "message": result_text 
        }), 500
