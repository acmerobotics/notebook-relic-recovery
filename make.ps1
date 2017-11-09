python ./scripts/convert.py
#todo spell check
python ./scripts/generate.py
cd out
latex notebook.tex -output-format=pdf
#run it twice to fix references
latex notebook.tex -output-format=pdf
cd ..