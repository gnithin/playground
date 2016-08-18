rm -r __pycache__
rm -r *.pyc
rm -r *.pyo

time python case1.py
time python case2.py

# Sample output
#$ zsh py2test.zsh
#rm: __pycache__: No such file or directory
#py2test.zsh:3: no matches found: *.pyo
#python case1.py  6.69s user 0.22s system 99% cpu 6.924 total
#python case2.py  6.68s user 0.22s system 99% cpu 6.924 total
