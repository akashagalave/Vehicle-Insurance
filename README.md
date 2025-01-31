# 🚀 MLOps Project: Streamlining ML Workflows

Welcome to the **MLOps Project**, a robust and scalable Machine Learning Operations framework designed to enhance ML lifecycle automation. This project integrates **modern tools, best practices, and CI/CD pipelines** to ensure seamless model development, deployment, and monitoring.

---

## 📌 Key Features

✔️ **pyproject.toml Integration** – Centralized dependency and project metadata management.
✔️ **CORS Configuration** – Seamless API communication across different origins.
✔️ **Asynchronous Execution** – Optimized performance for handling multiple requests.
✔️ **Self-Hosted GitHub Runner** – Persistent and automated CI/CD on AWS EC2.
✔️ **DVC for Data Versioning** – Efficient data tracking and reproducibility.
✔️ **Docker & Kubernetes** – Containerized deployments for scalability.

---

## 🚗 Vehicle Insurance Prediction
This project includes a **Vehicle Insurance Prediction** system that provides insights into insurance eligibility and premium estimations.

---

## 🔍 Understanding `pyproject.toml`

### ✅ What is `pyproject.toml`?
A modern **TOML-based configuration file** that standardizes Python project metadata and dependency management.

### ✨ Why is it important?
- Introduced with **PEP 518** to replace the outdated `setup.py`.
- **Centralizes metadata** (project name, version, dependencies, authors, etc.).
- Supports multiple **build systems** like `setuptools` and `poetry`.

### 📌 Breakdown of `pyproject.toml`
```toml
[project]  # Basic project information
name = "MyMLProject"
version = "0.1.0"
description = "A scalable ML model deployment framework."
authors = ["Your Name <your@email.com>"]

[tool.setuptools]  # Specifies setuptools for package building
packages = ["src"]

[tool.setuptools.dynamic]
dependencies = { file = "requirements.txt" }  # Links dependencies from requirements.txt
```

> **How does it work with other files?**
- `pyproject.toml` → Central place for project metadata and dependencies.
- `setup.py` → Optional for custom build steps.
- `requirements.txt` → Lists dependencies, referenced inside `pyproject.toml`.

---

## 🌍 Cross-Origin Resource Sharing (CORS)
CORS allows web applications to interact with APIs from different origins securely.

```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```
🔹 **Why?** Ensures seamless communication between frontend and backend applications.

---

## ⚡ Asynchronous Execution in Python
`async` enables non-blocking execution, improving application responsiveness.

```python
async def get_vehicle_data(self):
    form = await self.request.form()
```

🔹 **How it works?**
- `async` allows multiple tasks to execute concurrently.
- `await` ensures non-blocking operations for I/O tasks.

---

## 🔧 Setting Up a Persistent Self-Hosted Runner on AWS EC2
GitHub self-hosted runners can be configured as persistent services.

### 🔹 **Installation & Setup**
```bash
cd ~/actions-runner
sudo ./svc.sh install  # Install as a service
sudo ./svc.sh start    # Start the service
```

### 🔹 **Ensure Runner Persists After Reboot**
```bash
sudo systemctl enable actions.runner.<your-runner-name>.service
```

🔹 **Re-configure if needed:**
```bash
sudo ./svc.sh stop
sudo ./svc.sh uninstall
./config.sh --url https://github.com/your-repo --token <NEW_TOKEN>
```

---

## 📂 Project Structure
```
📦 MLOps-Project
 ┣ 📂 .dvc                        # DVC configurations and tracking
 ┣ 📂 .github/workflows           # CI/CD pipelines
 ┣ 📂 config                      # Configuration files
 ┣ 📂 data                        # Raw and processed data (tracked by DVC)
 ┣ 📂 logs                        # Logging and monitoring
 ┣ 📂 models                      # Saved models (tracked by DVC)
 ┣ 📂 notebook                    # Jupyter Notebooks for experiments
 ┣ 📂 src                         # Source code
 ┣ 📂 static/css                  # Frontend styles
 ┣ 📂 templates                   # HTML templates
 ┣ 📜 app.py                      # FastAPI backend
 ┣ 📜 demo.py                     # Data ingestion script
 ┣ 📜 pyproject.toml              # Project metadata & dependencies
 ┣ 📜 requirements.txt            # Dependency list
 ┣ 📜 setup.py                    # Setup script (if needed)
 ┣ 📜 Dockerfile                  # Containerization instructions
 ┣ 📜 dvc.yaml                    # DVC pipeline configuration file
 ┣ 📜 dvc.lock                    # DVC pipeline lock file (generated after pipeline run)
 ┣ 📜 .dvcignore                  # DVC ignore file (similar to .gitignore)

---

## 🚀 Get Started

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo.git
cd MLOps-Project
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Application**
```bash
uvicorn app:app --host 0.0.0.0 --port 5000
```

### 4️⃣ **Access the API**
Open your browser and visit:
```
http://localhost:5000/docs
```

---

## 📜 License
This project is **open-source** under the MIT License. Feel free to use, modify, and contribute!

🎯 **Built with Passion for Scalable ML Solutions** 🚀

