mkdir -p ~/.venv/megabank_api
python3 -m venv ~/.venv/megabank_api
source ~/.venv/megabank_api/bin/activate
python3 -m pip install -r requirements.txt
nohup python3 -m megabank_rest_api &

