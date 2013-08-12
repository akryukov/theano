import fontforge

base_name = "Theano"
fonts = ("Didot", "Modern", "OldStyle",)
style = "Regular"

def process_font(name, fname, style):
    filename = name  + fname  + "-" + style
    font = fontforge.open(filename + ".sfd")

    font.gasp_version = 1
    font.gasp = (
            ( 10   , ( 'antialias', 'symmetric-smoothing' ) ),
            ( 20   , ( 'gridfit', 'gridfit+smoothing' ) ),
            ( 65535, ( 'antialias', 'gridfit', 'symmetric-smoothing', 'gridfit+smoothing' ) ),
        )

    woff_meta = base_name + fname + "-WOFF-metadata.xml"
    f = file( woff_meta,'r' )
    lines = f.readlines()
    f.close()
    font.woffMetadata = "".join( lines )
    font.generate( filename + ".woff",layer="TTF" )

    font.encoding = "mac"
    font.generate(filename + ".ttf",flags=("opentype","old-kern","PfEd-colors","PfEd-lookups","dummy-dsig"),layer="TTF")

    font.em = 1000
    font.generate(filename + ".otf",flags=("opentype","PfEd-colors","PfEd-lookups"),layer="Fore")
    font.close()

for font in fonts:
    process_font(base_name, font, style)
