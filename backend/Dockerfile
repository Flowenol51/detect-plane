FROM python:3.9
WORKDIR /backend
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . ./

CMD ["export", "FLASK_APP=app"]
CMD ["flask", "run", "--port", "5000"]