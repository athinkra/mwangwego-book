cf = fontlab.CurrentFont()
delta = 0x16E00 - 0xF0000
for glyph in cf.values():
  unicode = glyph.unicode
  if( (unicode != None) and (unicode >= 0xF0000) ):
    glyph.unicode = unicode + delta
