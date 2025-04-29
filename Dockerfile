# Dockerfile

# Use a minimal Python image as the base
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
# RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# ENV PATH="/root/.cargo/bin:${PATH}"

# Copy only dependency files first (to leverage caching)
COPY pyproject.toml uv.lock ./

# Install project dependencies using uv
RUN uv pip install --system -r pyproject.toml

# Copy the rest of the application code
COPY . . 

# Expose the application port
EXPOSE 8000

# Run the application with uv
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]