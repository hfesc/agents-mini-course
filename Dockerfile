FROM python:3.11-slim-bookworm

WORKDIR /app

#RUN pip install langextract

#COPY demo_ollama.py .

ADD requirements.txt .
RUN pip install -r requirements.txt

#CMD ["python", "demo_ollama.py"]