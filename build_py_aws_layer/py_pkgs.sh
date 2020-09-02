pip install -r requirements.txt --no-cache-dir -t python/lib/python3.6/site-packages/
#find . -name "*.so" | xargs strip
#rm -rf python/lib/python3.6/site-packages/*.libs
rm -rf python/lib/python3.6/site-packages/*.dist-info
rm -rf python/lib/python3.6/site-packages/matplotlib
exit

