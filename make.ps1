python ./scripts/convert.py
python ./scripts/generate.py
cd out
latex notebook.tex -output-format=pdf
cd ..