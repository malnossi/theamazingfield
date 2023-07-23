# The Amazing Field

clone the repo:
```bash
git clone https://github.com/malnossi/theamazingfield.git
```

create vertualenv and install requirements
```bash
python3 -m venv venv
. /venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

run the server 
```bash
python manage.py runserver
```
and go to `http://localhost:8000/api/v1/employees/` to see how it works
