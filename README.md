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
`sudo nano /etc/crontab`
add script. Ex. to update dataset evry 2 minutes :
`*/2 * * * * cd /path/to/coronavirus-world-map/; bash script.sh`

For this you need to save Your Github credentials in your machine
## References

[Data sources] : https://www.worldometers.info/coronavirus/

[Medium link](https://medium.com/@amtam0/coronavirus-update-by-country-interactive-web-app-using-python-and-plotly-bac547386846?source=friends_link&sk=449aef56cfa9d71d681eb28371ce441d)
