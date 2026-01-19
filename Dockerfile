FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies into the system environment (no venv)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system --requirement pyproject.toml

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 8899

# Run the application
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8899"]
