FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./ ./
EXPOSE 5000
CMD ["uvicorn", "Server:app", "--host", "0.0.0.0", "--port", "5000"]
