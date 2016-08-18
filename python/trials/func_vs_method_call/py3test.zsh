rm -r __pycache__
rm -r *.pyc
rm -r *.pyo

time python3 case1.py
time python3 case2.py

# Sample output
#➜  func_vs_method_call git:(master) ✗
#$ zsh py3test.zsh
#rm: __pycache__: No such file or directory
#py3test.zsh:3: no matches found: *.pyo
#python3 case1.py  8.38s user 0.02s system 99% cpu 8.407 total
#python3 case2.py  7.97s user 0.02s system 99% cpu 7.996 total
