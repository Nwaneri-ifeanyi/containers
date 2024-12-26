FROM python:3.10

# Argument for versioning
ARG VERSION
LABEL org.label-schema.version=$VERSION

# Copy requirements.txt to the container
COPY ./requirements.txt /webapp/requirements.txt

# Set the working directory
WORKDIR /webapp

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Install specific scikit-learn version (1.2.2)
RUN pip install scikit-learn==1.2.2

# Copy application files to the container
COPY webapp/* /webapp

# Define the entry point and command
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
