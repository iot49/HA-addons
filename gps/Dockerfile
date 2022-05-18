ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
    python3 \
    py-pip

RUN pip install \
    pynmea2 \
    pyserial

COPY __main__.py /

CMD [ "python3", "/__main__.py" ]
