# Demo Flask App
Basic Flask App

## Getting Started

If this is your first Flask project:

1. Create basic Flask Application:

- Download Flask by pip:
  ```bash
  pip install flask=2.2.2

- Run app.py by this command:
  ```bash
  flask --app app run --debug

- Note:
  ```bash 
  Application default run at http://localhost:5000
  --debug help auto reload when code change

2. Return JSON from Flask

- Use dictionary (Flask auto convert to JSON):
  ```python
  @app.route("/json")
  def json_example():
    return {"message": "Hello, JSON!"}

- Use jsonify() (better way):
  ```python
  from flask import jsonify

  @app.route("/jsonify")
  def json_example2():
    return jsonify(message="Hello, JSON!")

3. Flask Configuration

- Use environment variable:
  ```bash
  export FLASK_APP=app.py
  export FLASK_ENV=development  # (Deprecated from Flask 2.3)

- Use app.config:
  ```python
  app.config["DEBUG"] = True
  app.config["SECRET_KEY"] = "mysecret"

4. Suggestion Structure

- Example:
  ```plaintext
  config.json
  requirements.txt
  setup.py
  src/
  ├── __init__.py
  ├── static/
  │   ├── css/
  │   │   └── main.css
  │   ├── img/
  │   │   └── header.png
  │   ├── js/
  │       └── site.js
  ├── templates/
  │   ├── about.html
  │   └── index.html
  tests/
  ├── test_auth.py
  └── test_site.py



## Contact

If you have any concern, feel free to contact me via:

- Gmail: huytuduelist@gmail.com
