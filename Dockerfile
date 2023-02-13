FROM python:3.10
ENV MONGO_URI 'uri'
RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile


CMD ["python3","api/app.py"]