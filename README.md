# 🚀 API REST - Gestión de Clientes, Facturas y Transacciones

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-Database-red)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green)

API REST desarrollada con **FastAPI**, **SQLModel** y **SQLite** para la gestión de **clientes**, **facturas** y **transacciones**.

---

# 📋 Características

- ✅ Gestión de clientes
- ✅ Gestión de facturas
- ✅ Registro de transacciones
- ✅ Base de datos SQLite
- ✅ Documentación automática con Swagger UI
- ✅ Arquitectura modular
- ✅ Validación de datos mediante SQLModel

---

# 📁 Estructura del Proyecto

```text
PYTHON_EVIDENCES_3407187/
│
├── app/
│   ├── main.py                 # Punto de entrada de la API
│   ├── conexion_bd.py          # Configuración de la base de datos
│   ├── listas.py               # Gestión de datos en memoria
│   │
│   ├── modelos/
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   └── enrutadores/
│       ├── clientes.py
│       ├── facturas.py
│       └── transacciones.py
│
├── bd_clientes.sqlite3
├── requierement.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Instalación

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Juanitodv28/PYTHON_EVIDENCES_3407187.git

cd PYTHON_EVIDENCES_3407187
```

---

## 2️⃣ Crear un entorno virtual

```bash
python -m venv venv
```

### Activar el entorno

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requierement.txt
```

---

## 4️⃣ Ejecutar la API

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en:

```
http://127.0.0.1:8000
```

---

# 📚 Documentación

Una vez iniciada la aplicación puedes acceder a la documentación interactiva:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🛠 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| 🐍 Python | Lenguaje principal |
| ⚡ FastAPI | Framework Web |
| 🗄 SQLModel | Modelado de datos |
| 💾 SQLite | Base de datos |
| 🚀 Uvicorn | Servidor ASGI |

---

# 📌 Comandos Git

| Acción | Comando |
|---------|----------|
| Clonar | `git clone <url>` |
| Ver historial | `git log --oneline` |
| Agregar cambios | `git add .` |
| Crear commit | `git commit -m "mensaje"` |
| Subir cambios | `git push origin main` |
| Revertir commit | `git revert <hash>` |

---

# 📖 Endpoints

## Clientes

- GET `/clientes`
- POST `/clientes`
- PUT `/clientes/{id}`
- DELETE `/clientes/{id}`

## Facturas

- GET `/facturas`
- POST `/facturas`
- PUT `/facturas/{id}`
- DELETE `/facturas/{id}`

## Transacciones

- GET `/transacciones`
- POST `/transacciones`
- PUT `/transacciones/{id}`
- DELETE `/transacciones/{id}`

---

# 👨‍💻 Autor

**Juan Pablo Sánchez Baquero**

Proyecto desarrollado como evidencia de aprendizaje del programa **Análisis y Desarrollo de Software** del **SENA**.

---

# ⭐ Si este proyecto te fue útil

¡No olvides dejar una estrella ⭐ en el repositorio!
