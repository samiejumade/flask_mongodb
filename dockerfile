FROM python:3.9-slim

ADD app.py /tree/app.py

ADD names.txt .

CMD ["python", "/tree/app.py"]
