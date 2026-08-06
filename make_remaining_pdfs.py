from fpdf import FPDF

documents = {
    "InfectionControl": """Infection Control Guidelines

All staff must wash hands before and after every patient interaction.
Personal protective equipment (PPE) including gloves and masks must be
worn in isolation wards.

Patients with contagious infections are placed in isolation rooms with
restricted visitor access.

Medical equipment must be sterilized between uses. Any staff member
showing symptoms of infection must report to occupational health
immediately and avoid direct patient contact.""",

    "InsurancePolicy": """Insurance Policy

Patients must provide a valid insurance card at the time of admission.
Pre-authorization is required for major procedures including surgeries
and MRI scans.

Claims must be submitted within 30 days of discharge. Required documents
include the discharge summary, itemized billing statement, and doctor's
referral letter.

For emergency admissions, insurance verification is completed after
initial treatment, not before.""",

    "ClinicalGuidelines": """Clinical Guidelines

All patient vitals must be recorded every 4 hours during admission.
Medication administration must be double-checked by two nurses before
being given to the patient.

ICU patients require continuous monitoring and vitals recorded every
30 minutes. Any adverse reaction to medication must be reported
immediately to the attending physician.

Discharge is only approved after the attending physician confirms
stable vitals for at least 24 hours.""",

    "DischargeProcess": """Discharge Process

Discharge planning begins 24 hours before the expected discharge date.
Patients receive a discharge summary including diagnosis, treatment
provided, and follow-up instructions.

Prescriptions for take-home medication are provided at discharge,
along with clear dosage instructions.

Patients must settle any outstanding bills or confirm insurance
coverage before final discharge paperwork is signed. Follow-up
appointments are scheduled before the patient leaves the hospital."""
}

for doc_name, content in documents.items():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.output(f"documents/{doc_name}.pdf")
    print(f"Created {doc_name}.pdf")

  