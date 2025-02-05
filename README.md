# Developing AI Application with Python & Flask

## 📌 Introduction
This repository contains code and resources for the **Developing AI Applications with Python and Flask** course on Coursera. The course covers the basics of Flask, integrating AI models, and deploying web applications.

## 📜 Course Overview
In this course, you will learn:
- How to build web applications using **Flask**.
- How to integrate **Machine Learning (ML) models** with Flask.
- How to handle HTTP **requests and responses**.
- How to deploy AI-powered Flask applications.

## 🛠️ Requirements
Before you begin, ensure you have the following installed:

- Python 3.7+
- Flask
- NumPy
- Pandas
- Scikit-learn
- TensorFlow / PyTorch (if using deep learning models)

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## 🚀 Getting Started
Follow these steps to set up and run the application:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/developing-ai-app-with-python-n-flask.git
   ```
2. Navigate to the project directory:
   ```bash
   cd developing-ai-app-with-python-n-flask
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## 📡 API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/`           | GET    | Returns a welcome message |
| `/predict`    | POST   | Accepts JSON input and returns AI model predictions |

Example request to `/predict`:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"data": [1.2, 3.4, 5.6]}'
```

## 📦 Deployment
To deploy this application, you can use:
- **Heroku**
- **AWS Lambda** (with Flask + Zappa)
- **Docker + Kubernetes**
- **Google Cloud Run**

## 📜 License
This project is licensed under the APACHE License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---

If you have any concern, don't hesitate to contact me via:

- Gmail: huytuduelist@gmail.com

🔥 **Happy Coding!** 🔥
