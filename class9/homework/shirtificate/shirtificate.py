from fpdf import FPDF

pdf = FPDF(orientation = "P", format = "A4", unit = "mm")
pdf.add_page()
pdf.set_font("helvetica", "B", 46)
pdf.cell(w = pdf.epw, txt = "CS50 Shirtificate", align = "C")
pdf.set_xy(0, 50)
pdf.image("shirtificate.png")
pdf.set_xy(10, 120)
pdf.set_font("helvetica", "B", 26)
pdf.set_text_color(255,255,255)
pdf.cell(w = pdf.epw, txt = "Ting Ai took CS50", align = "C")
pdf.output("shirtificate.pdf")
