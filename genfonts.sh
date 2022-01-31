#!/bin/bash

#####################################################################
#
# This file is part of Old Standard font family
# (http://www.thessalonica.org.ru/en/oldstandard.html) and is
# Copyright (C) 2006-2011 Alexey Kryukov <amkryukov@gmail.com>.
#
# This Font Software is licensed under the SIL Open Font License,
# Version 1.1.
#
# You should have received a copy of the license along with this Font
# Software. If this is not the case, go to (http://scripts.sil.org/OFL)
# for all the details including a FAQ.
#
#####################################################################/

ZIP="zip -DrX"
PACK_NAME=theano
DOCS="OFL.txt OFL-FAQ.txt FONTLOG.txt"
DOCS_SRC="theano-specimen.tex theano160.png"
VERSION="2.1"

rm -f *.zip *.aux *.log
#xelatex theano-specimen.tex
#xelatex theano-specimen.tex
#xelatex theano-specimen.tex

fontforge -script $PACK_NAME-generate.py

for f in *.ttf; do
    BASENAME=${f%.ttf}
    grcompiler -w3521 $BASENAME.gdl $BASENAME.ttf
    mv ${BASENAME}_gr.ttf $BASENAME.ttf
    #wine ~/bin/cachett.exe $f ${BASENAME}_hdmx.ttf Theano.cfg
    #mv ${BASENAME}_hdmx.ttf $BASENAME.ttf
    ttfautohint $BASENAME.ttf ${BASENAME}_ah.ttf
    mv ${BASENAME}_ah.ttf $BASENAME.ttf
done

$ZIP $PACK_NAME-$VERSION.ttf.zip  *.ttf $DOCS
$ZIP $PACK_NAME-$VERSION.otf.zip  *.otf $DOCS
$ZIP $PACK_NAME-$VERSION.woff.zip  *.woff $DOCS
$ZIP $PACK_NAME-$VERSION.src.zip genfonts.sh $PACK_NAME-generate.py *.gdl *.cfg *metadata.xml *.sfd $DOCS $DOCS_SRC
