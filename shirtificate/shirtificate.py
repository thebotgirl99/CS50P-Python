from fpdf import FPDF

name = input("Name: ").strip()

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

pdf.set_font("helvetica", "B", 50)
pdf.set_text_color(0, 0, 0)
pdf.cell(w=0, h=55, txt="CS50 Shirtificate", border=0, align="C")
pdf.ln()

pdf.image("shirtificate.png", x=10, y=80 , w=190)

pdf.set_font("helvetica", "B", size=26)
pdf.set_text_color(255, 255, 255)
pdf.cell(w=0, h=180, txt=f"{name} took CS50", border=0, align="C")

pdf.output("shirtificate.pdf")