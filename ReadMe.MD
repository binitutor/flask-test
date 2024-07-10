python --version

python -m venv venv

To activate env:
win -> venv\scripts\activate
macOs -> source venv/bin/activate

To deactivate env: 
win -> venv\scripts\deactivate
macOs -> deactivate

To update pip:
python -m pip install --upgrade pip

To install packages:
pip install -r requirements.txt

To output info of installed packages:
pip freeze > requirements.txt

To run api:
python src/api.py