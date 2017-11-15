Param([switch]$c)

If ($c) {
   python ./scripts/convert.py
   } Else {
   python ./scripts/convert.py
}

python ./scripts/generate.py
cd out
latex notebook.tex -output-format=pdf
#run it twice to fix references
latex notebook.tex -output-format=pdf
cd ..