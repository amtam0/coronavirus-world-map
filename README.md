## to setup and update the dataset

```bash script.sh```

To test the web-app locally :

```python -m http.server```

Open the link displayed

## to automate in AWS lambda

You need 2 layers:

- **python libraries** (Docker required):
```bash build_py_aws_layer/build_layer.sh```

- **Git** layer : check [link](https://github.com/lambci/git-lambda-layer) to get it 

The lambda function template is in the folder. Github Authentification username/password need to be added in the Lambda Env variables into the Console

You can then attach a timed trigger(Cloudwatchevent) to Lambda function to auto-update the dataset(here it is done every 5 hours).

Check [Medium link](https://medium.com/@amtam0/coronavirus-update-by-country-interactive-web-app-using-python-and-plotly-bac547386846?source=friends_link&sk=449aef56cfa9d71d681eb28371ce441d) for full setup

## Resources

[Data sources] : https://www.worldometers.info/coronavirus/
