#---------------------------------------------------------------------
# Install deps & add exec permissions
#---------------------------------------------------------------------

init:
	pip3 install -r requirements.txt
	chmod +x ./mtg_query.py
