FROM continuumio/miniconda3

EXPOSE 80

# Copy code
COPY ./ /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Install dependencies
RUN conda install cartopy shapely pip
RUN pip install -r requirements.txt

# Start service
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 refresh:app
