# Start from Playwright's official image (it has Python + browsers pre-installed)
FROM mcr.microsoft.com/playwright/python:v1.62.0-noble
# Set the working directory inside the container
WORKDIR /app

# copy the requirements file first (Docker caching trick)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Default command: run the tests
CMD ["pytest", "--html=reports/report.html", "--self-contained-html"]

