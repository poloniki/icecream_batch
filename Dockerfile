FROM python:3.12-slim
COPY requirements.txt requirements.txt
COPY tests tests/
COPY icecream icecream/
COPY setup.py setup.py
RUN pip install .
CMD uvicorn icecream.api:app --host 0.0.0.0 --port $PORT
