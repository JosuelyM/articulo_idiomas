articulo_plos_plantilla.pdf ::
cover_letter_draft.pdf ::
articulo.zip :: 
	make  articulo_plos_plantilla.pdf
	zip $@ articulo_plos_plantilla.tex articulo_plos_plantilla.bbl NW_A_ejes.png images/zipfFinal.pdf images/usoFinal.pdf images/Diversity.pdf images/dsFinal.pdf referencias.bib plos2015.bst

-include ~/makefile

# Repositorio: 
LOCALGITREPOSITORY=git@github.com:JosuelyM/articulo_idiomas.git




articulo_plos_gitdiff.pdf ::
	git checkout $(gitone)
	make articulo_plos_plantilla.pdf
	cp articulo_plos_plantilla.tex /tmp/v1.tex 
	git checkout master
	git checkout $(gittwo)
	cp articulo_plos_plantilla.tex /tmp/v2.tex 
	latexdiff /tmp/v1.tex /tmp/v2.tex > /tmp/v_diff.tex
	git checkout master
	pdflatex -draftmode /tmp/v_diff.tex
# 	bibtex cg_paper_gitdiff.aux
# 	pdflatex -draftmode cg_paper_gitdiff.tex
# 	pdflatex cg_paper_gitdiff.tex


articulo_plos_gitdiff_master_and_plos_v1.pdf ::
	make articulo_plos_gitdiff.pdf  gitone=plos_v1 gittwo=master

