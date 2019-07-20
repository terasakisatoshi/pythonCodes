c++ -O3 -shared -std=c++11  example.cpp -o example.so \
-I/usr/local/Cellar/python/3.6.5_1/Frameworks/Python.framework/Versions/3.6/include/python3.6m \
-I/usr/local/include/python3.6m \
-I/Users/terasakisatoshi/Library/Python/3.6/include/python3.6m \
-L/usr/local/opt/python/Frameworks/Python.framework/Versions/3.6/lib/python3.6/config-3.6m-darwin \
-lpython3.6m -ldl
