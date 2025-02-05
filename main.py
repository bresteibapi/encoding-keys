import subprocess

# Запуск FastAPI
fastapi_process = subprocess.Popen(
    ["uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8000"]
)

# Запуск Streamlit
streamlit_process = subprocess.Popen(["streamlit", "run", "./frontend/main.py"])

try:
    fastapi_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    fastapi_process.terminate()
    streamlit_process.terminate()
