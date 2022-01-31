# -*- coding: utf-8 -*-
from __future__ import print_function

import fontforge

base_name = "Theano"
fonts = ("Didot", "Modern", "OldStyle",)
styles = ("Regular", "Bold")

def process_font(name, fname, style):
    filename = "%s%s-%s" % (name, fname, style)
    if os.access (filename + ".sfd", os.R_OK):
	print ("Processing %s..." % (filename,))
        font = fontforge.open(filename + ".sfd")

        font.gasp_version = 1
        font.gasp = (
                ( 10   , ( 'antialias', 'symmetric-smoothing' ) ),
                ( 20   , ( 'gridfit', 'gridfit+smoothing' ) ),
                ( 65535, ( 'antialias', 'gridfit', 'symmetric-smoothing', 'gridfit+smoothing' ) ),
            )

        woff_meta = "%s%s-%s-WOFF-metadata.xml" % (base_name, fname, style)
        f = file( woff_meta,'r' )
        lines = f.readlines()
        f.close()
        font.woffMetadata = "".join( lines )
        font.generate( filename + ".woff",layer="TTF" )

        font.encoding = "mac"
        font.generate(filename + ".ttf",flags=("opentype","old-kern","winkern","dummy-dsig"),layer="TTF")

        font.em = 1000
        font.generate(filename + ".otf",flags=("opentype"),layer="Fore")
        font.close()

for font in fonts:
    for style in styles:
        process_font(base_name, font, style)
