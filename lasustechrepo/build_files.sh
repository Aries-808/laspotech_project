# build_files.sh
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install django
# make migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate 
python3.9 manage.py collectstatic
python3.9 manage.py runserver
