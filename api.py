from flask import Flask, jsonify, request
import json

app = Flask(__name__)
model = None

def init_api(trained_model):
    global model
    model = trained_model

@app.route("/analyzeNote", methods=["POST"])
def post_analyze_note():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "Missing 'text' in request body"}), 400

    success, result_text = model.analyzeNote(data["text"])
    
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
    
@app.route("/groupCard", methods=["POST"])
def post_group_card():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "Missing 'text' in request body"}), 400

    success, result_text = model.analyzeNote(data["text"])
    
    if success:
        try:
            data = json.loads(result_text.strip())

            return jsonify({
                "status": "success",
                "data": data
            })
        except json.JSONDecodeError:
            return jsonify({
                "status": "error",
                "message": "The AI failed to format the response correctly.",
                "raw_output": result_text
            }), 500
        
    else:
        return jsonify({
            "status": "error",
            "message": result_text 
        }), 500
