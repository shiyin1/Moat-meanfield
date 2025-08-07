#!/bin/bash

rm *.mp
latex feyn.tex && mpost *.mp && latex feyn.tex
chmod 777 pictures.sh
./pictures.sh
rm fmf.*
rm *.aux
#rm *.bbl
#rm *.out
#rm *.toc
rm *.log
rm *.dvi
rm pictures.sh
