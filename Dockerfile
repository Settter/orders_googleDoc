FROM python:3.10.7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /orders_googleDoc
WORKDIR /orders_googleDoc
ENTRYPOINT ["python"]
CMD ["App.py"]