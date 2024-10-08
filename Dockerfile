FROM python:3.8

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip install -r requirements.txt

COPY webapp/* /webapp

EXPOSE 80

ENTRYPOINT [ "uvicorn" ]

CMD [ "--host", "0.0.0.0", "--port", "80", "main:app" ]

