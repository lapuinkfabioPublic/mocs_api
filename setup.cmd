rem #Fabio Leandro Lapuinka
rem Setup mínimo para instalacao API MOC

python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
