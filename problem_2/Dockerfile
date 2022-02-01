FROM python:3.9
RUN mkdir -p /flask/app
WORKDIR /flask/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]

