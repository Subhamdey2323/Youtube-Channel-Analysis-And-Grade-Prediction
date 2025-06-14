FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir streamlit numpy pandas scikit-learn

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


# for running the docker image and container

# docker build -t youtube-streamlit .
# docker run -p 8501:8501 youtube-streamlit
