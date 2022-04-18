-include ~/makefile

%.pdf :: %.tex
	pdflatex --halt-on-error $<
	pdfcrop $@
# 	pdfcrop $(basename $<).pdf
	mv $(basename $<)-crop.pdf $(basename $<).pdf
	cp $(basename $<).pdf /tmp/
# 	killall -1 mupdf

