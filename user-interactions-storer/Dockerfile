FROM python:3.10

COPY src /user-interactions-storer
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "/user-interactions-storer/main.py"]
