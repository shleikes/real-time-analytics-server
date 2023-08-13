FROM python:3.10

COPY fake_data_injector.py /fake_data_injector.py
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "/fake_data_injector.py"]
