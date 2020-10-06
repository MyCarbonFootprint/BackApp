ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-alpine

# Install dependenties
RUN apk --update add --no-cache \
    gcc \
    python3-dev \
    musl-dev

# Create working directory
RUN mkdir -p /app
WORKDIR /app

# Install requirements
COPY setup.py setup.py
RUN pip3 install --no-cache-dir  -e .

# Copy sources
COPY app app

# Copy start script
COPY config/start.sh start.sh
RUN chmod +x start.sh

# Variables
ENV FLASK_APP app
ENV TZ Europe/Paris

# Expose port
EXPOSE 5000

CMD [ "./start.sh" ]
