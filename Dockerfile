FROM python:3.13.0b1-slim

COPY ./ /opt/todo-test

WORKDIR /opt/todo-test

RUN pip3 install -r requirements.txt

EXPOSE 5001/tcp

CMD ["python3", "./server/app.py"]
