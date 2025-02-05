# Lab 1

## Learning Objectives 

After completing this lab, you will be able to:

- Create and run a Flask server in development mode
- Return JSON from an endpoint
- Understand the request object

Tutorial:

- Firstly, run server by this command:
  ```bash
  flask --app server --debug run

- If you want to send a http request GET to running server at:localhost:5000 and response, you can use this command:
- In Linux:
  ```bash
  curl -X GET -i -w "\n" http://localhost:5000

- In Windows:
  ```bash
  curl.exe -X GET -i -w "\n" http://localhost:5000