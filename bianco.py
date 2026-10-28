from pypdf import PdfWriter

w = PdfWriter()
for _ in range(100):
    w.add_blank_page(width=595.276, height=841.89)  # A4 in punti

with open("bianco.pdf", "wb") as f:
    w.write(f)
