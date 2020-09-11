FROM python:3.8-alpine
MAINTAINER chladond "chladond@fit.cvut.cz"
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
