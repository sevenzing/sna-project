FROM python:3.9
COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY backend /app

CMD ["python", "main.py"]
