FROM python:3.13-alpine

WORKDIR /app

COPY backend/ /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]


