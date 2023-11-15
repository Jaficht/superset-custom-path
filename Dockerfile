FROM apache/superset:latest

# Install sqlalchemy-bigquery
RUN pip install sqlalchemy-bigquery