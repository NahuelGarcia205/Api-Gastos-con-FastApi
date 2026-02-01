

# 💸 Gestor de Gastos en Python

Proyecto personal para practicar Python de forma realista y progresiva, aplicando buenas prácticas de desarrollo como control de versiones con Git, uso de entornos virtuales y backend con FastAPI.

---

## 🚀 Tecnologías utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn
- Git & GitHub
- Entorno virtual (venv)

---

## 📂 Estructura del proyecto

├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
└── venv/

---

## 🛠️ Configuración del entorno

### Crear entorno virtual

1-python -m venv venv
2-Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
3-.\venv\Scripts\activate

---

### ⚙️ Instalación y ejecución de las librerias
pip install -r requirements.txt

---

### Ejecutar el Servidor
uvicorn main:app --reload
