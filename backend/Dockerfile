# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /backend
RUN pip3 install distro-info==1.0
CMD ["sudo", "apt-get", "install", "libssl-dev", "libcurl4-openssl-dev", "python-dev"] 
#Line 6 should fix the "no such file or directory: 'curl-config'" but it does not for some reason
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . ./

CMD ["export", "FLASK_APP=app"]
CMD ["flask", "run", "--port", "5000"]