FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH "${PYTHONPATH}"
ENV API_TOKEN "${API_TOKEN}"
CMD [ "python3", "sample_currency.py", "--currency", "EUR", "--period", "5", "--time", "1"]