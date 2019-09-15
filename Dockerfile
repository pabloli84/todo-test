FROM python:3-slim

WORKDIR /opt/app
COPY ./ /opt/app

RUN pip install -r requirements.txt

EXPOSE 5001/tcp

CMD ["python", "./server/app.py"]