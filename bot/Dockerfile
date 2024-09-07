FROM python:3.12

WORKDIR /workdir

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD python main.py

