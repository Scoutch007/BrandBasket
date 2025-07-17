import pandas as pd
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_csv(results):
    df = pd.DataFrame(results)
    return df.to_csv(index=False).encode("utf-8")

def generate_pdf(results):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    
    table_data = [["Product", "Supermarket", "Price", "Unit Price", "URL"]]
    for item in results:
        table_data.append([
            item["name"],
            item["supermarket"],
            f"£{item['price']:.2f}",
            f"£{item.get('unit_price', '-')}/" + (item.get("unit_type") or "-"),
            item["url"]
        ])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    doc.build([Paragraph("UK Supermarket Price Comparison", styles["Title"]), table])
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
