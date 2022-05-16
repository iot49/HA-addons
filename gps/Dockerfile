ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3

RUN pip install pynmea2

COPY __main__.py /

CMD [ "python3", "/__main__.py" ]