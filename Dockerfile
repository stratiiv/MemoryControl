FROM python:3.11
WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3","-u","app.py"]