FROM python:3.10

COPY src /analytics-engine
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "/analytics-engine/main.py"]
