FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY walmart_scrap.py /app/walmart_scrap.py

VOLUME /app/data

CMD ["python", "walmart_scrap.py"]
