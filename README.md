## to setup and update the dataset

```bash script.sh```

To test the web-app locally :

```python -m http.server```

Open the link displayed

## to automate in AWS lambda

You need 2 layers
- **python libraries** (Docker required):
```bash build_py_aws_layer/build_layer.sh```
<<<<<<< HEAD
- **Git** layer : check [link]() to get it 
=======
- **Git** layer : check [link](https://github.com/lambci/git-lambda-layer) to get it 
>>>>>>> a00e00a854dd51dad910cd29a25dfec75780c26a

The lambda function template is in the folder. Github Authentification username/password need to be added in the env variables in the Console

You can then add a timed trigger(Cloudwatchevent) to lambda in order to automatically update the dataset(here it is updated every 5 hours).

## References

[Data sources] : https://www.worldometers.info/coronavirus/

[Medium link](https://medium.com/@amtam0/coronavirus-update-by-country-interactive-web-app-using-python-and-plotly-bac547386846?source=friends_link&sk=449aef56cfa9d71d681eb28371ce441d)
