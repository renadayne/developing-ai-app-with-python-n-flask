# ✨ Tóm tắt & Giải thích Flask Request và Response Object ✨

---

## **1⃣ Request Object (Đối tượng Yêu cầu) 📢**
Flask cung cấp một **Request Object** để truy cập thông tin từ client.

### **🔹 Các thành phần quan trọng trong Request Object:**
- **Headers**: Chứa thông tin về request (User-Agent, Host, Cache-Control,...).
- **URL**: Địa chỉ được yêu cầu.
- **Query Parameters**: Dữ liệu từ URL (`/search?query=flask` → `query="flask"`).
- **Body**: Dữ liệu gửi từ client (thường là JSON hoặc form).
- **Cookies**: Cookie do client gửi kèm.
- **Secure Connection**: Kiểm tra xem request có dùng HTTPS không (`is_secure`).

### **📝 Ví dụ:**
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    data = request.args.get('query')  # Lấy query param
    json_data = request.get_json()  # Lấy body JSON nếu có
    return {"query": data, "json": json_data}

if __name__ == '__main__':
    app.run(debug=True)
```
- Nếu gửi **GET** với URL: `/data?query=flask` → Trả về `{ "query": "flask", "json": None }`
- Nếu gửi **POST** với JSON body: `{"name": "Flask"}` → Trả về `{ "query": None, "json": {"name": "Flask"} }`

---

## **2⃣ Response Object (Đối tượng Phản hồi) 📤**
Flask tự động tạo một **Response Object** để gửi phản hồi về client.

### **🔹 Các thuộc tính quan trọng của Response Object:**
- **status_code**: Mã trạng thái HTTP (200 OK, 404 Not Found, 500 Internal Server Error...).
- **headers**: Chứa thông tin phản hồi (Content-Type, Content-Length, Expires,...).
- **content_type**: Loại dữ liệu được trả về (`application/json`, `text/html`).
- **cookies**: Có thể đặt hoặc xóa cookie trên client.

### **📝 Ví dụ:**
```python
from flask import Flask, jsonify, make_response, redirect

app = Flask(__name__)

@app.route('/json')
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
```
- Truy cập `/json` → Trả về JSON `{"message": "Hello, Flask!"}`
- Truy cập `/custom_response` → Trả về response với status **201 Created** + header tùy chỉnh
- Truy cập `/redirect_example` → **Chuyển hướng** đến `/json`

---

## **3⃣ Tổng Kết ✨**
✅ **Request Object** giúp đọc dữ liệu từ client (URL, headers, body, cookies).  
✅ **Response Object** giúp gửi phản hồi về client (status, headers, content).  
✅ Flask cung cấp `jsonify()`, `make_response()`, `redirect()`, `abort()` để tùy chỉnh phản hồi.


