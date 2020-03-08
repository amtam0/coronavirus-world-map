## to setup

`virtualenv -p python3 corona-env`

`source corona-env/bin/activate`

`pip install -r requirements.txt`

## to run

`bash script.sh`

To test locally :

`python -m http.server`

open the link displayed

## to automate with Cron (crontab -e in root)

Ex. to update dataset evry 2 minutes :

`*/2 * * * * cd /path/to/coronavirus-world-map/; bash script.sh`

## References

[Data sources] : https://www.worldometers.info/coronavirus/
