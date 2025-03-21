FROM python:3.11

# Set the workdir where we run all commands
WORKDIR /code/crud_api/

# Copy the code and project files to a standard location
COPY src pyproject.toml README.md /code/crud_api/

# Install the crud_api module
RUN python -m pip install .

# Run the API (the default API port is 8000)
ENTRYPOINT [ "python", "-m", "crud_api", "--port", "8000" ]

