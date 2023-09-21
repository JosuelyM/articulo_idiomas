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
	latexpand cg_paper.tex -o /tmp/cg_paper_expanded_one.tex
	git checkout master
	git checkout $(gittwo)
	latexpand cg_paper.tex -o /tmp/cg_paper_expanded_two.tex
	latexdiff /tmp/cg_paper_expanded_one.tex /tmp/cg_paper_expanded_two.tex > cg_paper_gitdiff.tex
	git checkout master
	pdflatex -draftmode cg_paper_gitdiff.tex
	bibtex cg_paper_gitdiff.aux
	pdflatex -draftmode cg_paper_gitdiff.tex
	pdflatex cg_paper_gitdiff.tex


cg_paper_gitdiff_PRL_1_and_2.pdf ::
	make cg_paper_gitdiff.pdf  gitone=prlv1 gittwo=prlv3

