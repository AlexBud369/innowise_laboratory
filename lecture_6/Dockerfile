# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create SQLite database file with write permissions
RUN touch books.db && chmod 666 books.db

# Start the application
CMD ["uvicorn", "book_api.main:app", "--host", "0.0.0.0", "--port", "80"]