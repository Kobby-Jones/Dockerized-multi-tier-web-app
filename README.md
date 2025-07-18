
# ⚙️ Dockerized Multi-Tier Web App

A fully Dockerized **multi-tier web application** showcasing a real-world DevOps project with a clean separation of frontend, backend, and database layers — perfect for scalable deployments and container orchestration.

This project is built for DevOps learners, recruiters, and anyone interested in modern deployment workflows using Docker and Docker Compose.

---

## 🚀 Why This Project Stands Out

✅ Real-world microservice-style architecture  
✅ End-to-end containerization using Docker  
✅ Easy to replicate, scale, and build upon  
✅ Excellent portfolio and DevOps showcase

---

## 🧱 Architecture Overview

```plaintext
|--------------------|       |-------------------|       |---------------------|
|   Frontend (UI)    | <---> |   Backend (API)   | <---> |   Database (MySQL)  |
|  HTML / CSS / JS   |       |    Python / Flask |       |     MySQL / MariaDB |
|--------------------|       |-------------------|       |---------------------|
````

---

## 🛠 Tech Stack

<div align="center">

  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend-Flask%20(Python)-lightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Database-MySQL-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Docker-Orchestrated-blue?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/DevOps-Ready-success?style=for-the-badge" />

</div>

---

## 📁 Project Structure

```
Dockerized-multi-tier-web-app/
│
├── frontend/          # Static site files
│   └── index.html
│
├── backend/           # Flask app with API routes
│   ├── app.py
│   └── requirements.txt
│
├── db/                # (Optional) DB init or seed files
│
├── docker-compose.yml # Multi-container orchestration
└── README.md
```

---

## 🐳 How to Run the App Locally

Make sure you have Docker and Docker Compose installed.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kobby-Jones/Dockerized-multi-tier-web-app.git
cd Dockerized-multi-tier-web-app
```

### 2️⃣ Build and Start All Containers

```bash
docker-compose up --build
```

This will:

* Serve the frontend on [http://localhost:3000](http://localhost:3000)
* Expose the Flask backend API on [http://localhost:5000](http://localhost:5000)
* Run the MySQL database in the background

### 3️⃣ Test the App

* Access the frontend UI in a browser
* Test the API endpoints (e.g., `/api/status`) via browser or Postman
* Verify backend ↔ database communication in the logs

---


## ✨ Highlights

* Multi-tier web app with Docker Compose
* Each service runs in its own container
* MySQL database with persistent networking
* Reusable and production-ready structure

---

## 📦 What You’ll Learn / Showcase

* Docker networking between containers
* Orchestrating a full-stack app using Docker Compose
* Managing service dependencies
* Infrastructure separation for scalability
* How to run and test multi-container environments locally

---

## 🧹 Stop the App

When you're done:

```bash
docker-compose down
```

---

## 📚 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Cobbina Emmanuel (Kobby Jones)**
[![GitHub](https://img.shields.io/badge/GitHub-Kobby--Jones-black?style=flat-square\&logo=github)](https://github.com/Kobby-Jones)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square\&logo=linkedin)](https://www.linkedin.com/in/cobbina-emmanuel-376072209/)

---

## 💡 Want to Contribute?

Pull requests are welcome!
If you have suggestions for improvement or want to extend the backend logic, feel free to fork and contribute.

---

## ⭐️ Give It a Star!

If you found this project useful, inspiring, or educational — drop a ⭐ on the repo!

