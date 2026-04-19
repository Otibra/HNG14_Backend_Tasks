# Gender Classification API (Django REST Framework)

## 📌 Overview

This is a Django REST API that predicts the gender of a given name using an external API.

The API accepts a name as input and returns:

* predicted gender
* probability score
* supporting data count


## 🔗 Endpoint

```
GET /api/classify/?name=<name>

## 📥 Request Example

```
GET /api/classify/?name=Brian
```

---

## 📤 Successful Response

```json
{
  "status": "success",
  "name": "Brian",
  "gender": "male",
  "probability": 0.99
}
```

---

## ❌ Error Response

If the `name` parameter is missing:

```json
{
  "status": "error",
  "message": "Missing or empty name parameter"
}
```

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* External API (genderize.io)
* Vercel (Deployment)

### 4. Run the server

```
python manage.py runserver
```

---

### 5. Test locally

```
http://127.0.0.1:8000/api/classify/?name=Brian
```

---

## 📁 Project Structure

```
project/
├── api/
│   └── index.py
├── api_integration_data_processing/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── vercel.json
```

---

## ✨ Features

* Name-based gender prediction
* Input validation
* Error handling
* RESTful API design
* Deployed on Vercel

---

## ⚠️ Notes

* Ensure `name` parameter is always provided in requests
* Deployment requires proper Vercel configuration (`api/index.py`, `vercel.json`)
* Environment variables should be used for sensitive data like `SECRET_KEY`

---

## 👤 Author

**Brian Otieno**

---

## 📜 License

This project is open-source and available for learning and educational purposes.
