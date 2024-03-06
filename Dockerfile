FROM python:3.8.10-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && poetry config virtualenvs.create false

RUN /root/.cargo/bin/uv pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5001

# Command to run the application (assuming it's a Flask app)
CMD ["streamlit", "run","main.py"]  # Replace with your application's entry point if different

# Alternative command for uvicorn (if your application uses it)
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]

