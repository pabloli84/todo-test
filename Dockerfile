FROM python:3.9-slim

COPY ./ /opt/todo-test

WORKDIR /opt/todo-test

RUN pip3 install -r requirements.txt

EXPOSE 5001/tcp

CMD ["python3", "./server/app.py"]
