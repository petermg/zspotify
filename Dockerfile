#  FROM python:3.9-alpine as base

FROM jsavargas/zspotify as base

RUN apk --update add git ffmpeg

FROM base as builder

WORKDIR /install

COPY requirements.txt /requirements.txt
RUN apk add gcc libc-dev zlib zlib-dev jpeg-dev \
    && /usr/local/bin/python -m pip install --upgrade pip && pip install --prefix="/install" -r /requirements.txt


FROM base

WORKDIR /app
COPY --from=builder /install /usr/local

COPY zspotify.py /app

VOLUME /download /config

ENTRYPOINT ["/usr/local/bin/python3", "zspotify.py"]

