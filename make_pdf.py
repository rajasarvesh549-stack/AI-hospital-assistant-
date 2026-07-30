from fpdf import FPDF

content = """Patient Admission Policy

All patients must register at the front desk before admission.
A valid government ID and insurance card (if applicable) are required.

For emergency admissions, patients are admitted immediately, and
documentation is completed within 24 hours.

For planned admissions, patients must arrive at least 2 hours before
the scheduled procedure and complete pre-admission paperwork,
including consent forms and medical history.

The admission desk is open 24/7 for emergencies, and 8 AM to 8 PM
for planned admissions."""

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 10, content)
pdf.output("documents/PatientAdmission.pdf")

print("PDF created successfully!")
