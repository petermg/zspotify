FROM python:3.8



WORKDIR /app
COPY requirements.txt requirements.txt

RUN apt-get update && \
	apt-get install -y \
	git \
	ffmpeg \
	python3-pip && \
	python3.8 -m pip install --upgrade pip && \
	pip3.8 install -r requirements.txt  && \
	apt-get remove --purge -y build-essential && \
	apt-get autoclean -y && apt-get autoremove -y 



COPY zspotify.py /app/zspotify.py
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod 777 /app/zspotify.py 
RUN chmod 777 /app/entrypoint.sh 

VOLUME /download /config

WORKDIR /config
ENTRYPOINT /app/entrypoint.sh
