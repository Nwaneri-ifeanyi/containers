FROM python:3.9.21
COPY ./requirements.txt /webapp/requirements.txt
WORKDIR /webapp
RUN pip install -r requirements.txt
COPY webapp/* /webapp
COPY webapp/roberta-sequence-classification-9.onnx /webapp
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
