FROM python:3.12-slim-bullseye

WORKDIR /app

COPY /src /app

EXPOSE 8080

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "./Home.py", "--server.port=8080"]