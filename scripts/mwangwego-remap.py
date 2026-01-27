from docx.text.paragraph import Paragraph
from docx.document import Document
from docx.table import _Cell, Table
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
import docx
import sys

def iter_block_items(parent):
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            table = Table(child, parent)
            for row in table.rows:
                for cell in row.cells:
                    yield from iter_block_items(cell)
                    
def main():
	oldMwangwego = list( range(0xF0000, 0xF0040) )
	newMwangwego = list( range(0x16E00, 0x16E40) )
	# print ( len(oldShaaldaa) )
	# print ( len(newShaaldaa) )
	old = "".join( map(chr, oldMwangwego) )
	new = "".join( map(chr, newMwangwego) )
	mytable = str.maketrans(old, new)

	indoc = sys.argv[1]
	outdoc = sys.argv[1].replace( ".docx", "-Out.docx" )
	doc = docx.Document( indoc )
	for block in iter_block_items(doc):
		inline = block.runs
		for j in range(len(inline) ):
			oldText = inline[j].text
			newText = oldText.translate(mytable)
			inline[j].text = newText

	doc.save( outdoc )

if __name__ == "__main__":
    main()
