rm -f source/*.rst
sphinx-apidoc -F -o source ../src
rm -rf build
make html