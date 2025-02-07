from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=["GET", "POST"])
def get_data():
    print(f"Headers: {request.headers}")  # Debug headers
    print(f"Raw data: {request.data}")    # Debug raw body

    # if request.content_type != "application/json":
    #     return jsonify({"error": "Content-Type must be application/json"}), 415

    json_data = request.get_json(silent=True)  # Silent tránh lỗi nếu không phải JSON
    return jsonify({"json": json_data})

if __name__ == '__main__':
    app.run(debug=True)
