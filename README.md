# Local
```
python -m venv virtualenv
.\virtualenv\Scripts\activate
pip install -r requirements.txt

python app.py
```

# Docker

`docker build . -t flask`
`docker run -it -p 5000:5000 flask`

Access webserver at: `localhost:5000`