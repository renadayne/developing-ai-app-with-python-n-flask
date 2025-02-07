from flask import Flask, jsonify, make_response, redirect

app = Flask(__name__)

@app.route('/json', methods=["GET", "POST"])
def json_response():
    return jsonify(message="Hello, Flask!")  # Flask tự động tạo Response object

@app.route('/custom_response')
def custom_response():
    response = make_response("Custom Response", 201)
    response.headers["Custom-Header"] = "MyValue"
    return response  # Trả về phản hồi tùy chỉnh

@app.route('/redirect_example')
def redirect_example():
    return redirect('/json')  # Redirect tới /json

if __name__ == '__main__':
    app.run(debug=True)