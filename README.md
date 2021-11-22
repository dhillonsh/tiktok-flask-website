# Local
```
python -m venv virtualenv
virtualenv/Scripts/activate.bat

python app.py
```

# Docker

`docker build . -t flask`
`docker run -it -p 5000:5000 flask`

Access webserver at: `localhost:5000`