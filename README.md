# Public API for HNG12 Stage 0 – Backend Task  

https://hng.tech/hire/python-developers

## Introduction  
This is a simple public API built using **Flask** to fulfill the **HNG12 Stage 0 Backend Task**. The API provides the following JSON response:  

- Your **registered email address** (used for HNG12 Slack registration).  
- The **current datetime** in **ISO 8601** format (UTC).  
- The **GitHub repository URL** of the project.  

## Features  
- **Flask** framework for building the API.  
- **Flask-CORS** for Cross-Origin Resource Sharing.  
- **dotenv** for environment variable management.  

- Fast response time (< 500ms).  

---

## API Specification  

### **Endpoint**  
```http
GET https://hng12-stage0-backend-77lu.onrender.com/api/v1/information
```

### **Response Format (200 OK)**  
```json
{
  "email": "your-email@example.com",
  "current_datetime": "current-time",
  "github_url": "www.github.com/Favouridowu02/hng12_stage0_backend"
}
```

### **Response Fields**  
| Field Name         | Type   | Description                                      |  
|--------------------|--------|--------------------------------------------------|  
| `email`           | String | Your registered HNG12 email.                     |  
| `current_datetime` | String | Dynamically generated UTC timestamp (ISO 8601). |  
| `github_url`      | String | Public GitHub repository URL.                   |  

---

## Getting Started  

### **Prerequisites**  
Ensure you have the following installed on your system:  
- **Python 3.x**  
- **Git**  
- **Flask, Flask-CORS, python-dotenv**  

### **Setup Instructions**  

#### **1. Clone the Repository**  
```bash
git clone https://www.github.com/Favouridowu02/hng12_stage0_backend
cd hng12_stage0_backend
```

#### **2. Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

#### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

#### **4. Create a `.env` File**  
Inside the project directory, create a **.env** file and add the following:  
```
EMAIL=your-email@example.com
GITHUB_URL=https://github.com/yourusername/your-repo
```

---

## Running the Project  

#### **1. Start the Flask Server**  
```bash
python3 -m api.v1.app
```

#### **2. Test the API**  
Open your browser or use Postman to send a **GET request** to:  
```http
http://127.0.0.1:5000/api/v1/information
```

### **Example Response**  
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Example Usage  
Once deployed, access your API via:  
```http
GET /api/v1/information
```
