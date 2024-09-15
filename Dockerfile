FROM python:3.10.0-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

ENV stations="{'новодачная': '29304', 'лианозово': '29104'}"

ENV pythonpath=/app/src

ENTRYPOINT ["python", "src/main.py"]
