FROM python:3.10
ENV MONGO_URI 'uri'
RUN mkdir -p /home/app
COPY . /home/app
RUN pip install pipenv
RUN pipenv sync 
CMD ["python3","-m","api/app.py"]