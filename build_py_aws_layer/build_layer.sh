docker run -v ${PWD}:/var/task lambci/lambda:build-python3.6 bash py_pkgs.sh
zip -r mypythonlibs36.zip python
rm -rf python/
