## to setupe and update dataset

`bash script.sh`

To test locally :

`python -m http.server`

open the link displayed

## to automate in AWS lambda

You need two layers
- python packages you can build it (Docker required):
`bash build_py_aws_layer/build_layer.sh`
- 

You can then add a timed trigger to automatically update the dataset

## References

[Data sources] : https://www.worldometers.info/coronavirus/

[Medium link](https://medium.com/@amtam0/coronavirus-update-by-country-interactive-web-app-using-python-and-plotly-bac547386846?source=friends_link&sk=449aef56cfa9d71d681eb28371ce441d)
