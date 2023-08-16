articulo_plos_plantilla.pdf ::
cover_letter_draft.pdf ::
articulo.zip :: 
	make  articulo_plos_plantilla.pdf
	zip $@ articulo_plos_plantilla.tex articulo_plos_plantilla.bbl NW_A_ejes.png images/zipfFinal.pdf images/usoFinal.pdf images/Diversity.pdf images/dsFinal.pdf referencias.bib plos2015.bst

-include ~/makefile

# Repositorio: 
LOCALGITREPOSITORY=git@github.com:JosuelyM/articulo_idiomas.git
