
from flask import Flask, request, jsonify
from matcher import analyze_resume_pdf

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    result = analyze_resume_pdf(file)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
