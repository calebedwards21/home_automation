FROM python:3.7-alpine
WORKDIR /code
COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ../web_scraper/influx.py ./
EXPOSE 5000
COPY . .
CMD [ "python", "./influx.py"]