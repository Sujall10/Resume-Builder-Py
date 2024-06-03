import tkinter as tk
from tkinter import simpledialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

def get_user_input():
    data = {}
    data['name'] = simpledialog.askstring("Input", "Enter your name:")
    data['address'] = simpledialog.askstring("Input", "Enter your address:")
    data['phone'] = simpledialog.askstring("Input", "Enter your phone number:")
    data['email'] = simpledialog.askstring("Input", "Enter your email:")
    data['profile'] = simpledialog.askstring("Input", "Enter your profile summary:")

    experience = []
    while True:
        title = simpledialog.askstring("Input", "Enter your job title (or 'done' to finish):")
        if title.lower() == 'done':
            break
        company = simpledialog.askstring("Input", "Enter the company name:")
        years = simpledialog.askstring("Input", "Enter the years you worked there:")
        description = simpledialog.askstring("Input", "Enter a description of your work:")
        experience.append({
            'title': title,
            'company': company,
            'years': years,
            'description': description
        })
    data['experience'] = experience

    education = []
    while True:
        degree = simpledialog.askstring("Input", "Enter your degree (or 'done' to finish):")
        if degree.lower() == 'done':
            break
        institution = simpledialog.askstring("Input", "Enter the institution name:")
        years = simpledialog.askstring("Input", "Enter the years you studied there:")
        education.append({
            'degree': degree,
            'institution': institution,
            'years': years
        })
    data['education'] = education

    skills = simpledialog.askstring("Input", "Enter your skills (comma-separated):").split(',')
    data['skills'] = [skill.strip() for skill in skills]

    return data

def generate_resume(data, output_path='resume.pdf'):
    pdf = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    title_style = styles['Title']
    elements.append(Paragraph(data['name'], title_style))
    elements.append(Spacer(1, 12))

    contact_info = f"{data['address']}<br/>{data['phone']}<br/>{data['email']}"
    elements.append(Paragraph(contact_info, styles['Normal']))
    elements.append(Spacer(1, 12))

    profile_style = ParagraphStyle(name='Profile', fontSize=12, leading=14)
    elements.append(Paragraph('Profile', styles['Heading2']))
    elements.append(Paragraph(data['profile'], profile_style))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph('Experience', styles['Heading2']))
    for exp in data['experience']:
        elements.append(Paragraph(f"<b>{exp['title']}</b> at {exp['company']}", styles['Normal']))
        elements.append(Paragraph(exp['years'], styles['Italic']))
        elements.append(Paragraph(exp['description'], styles['Normal']))
        elements.append(Spacer(1, 12))

    elements.append(Paragraph('Education', styles['Heading2']))
    for edu in data['education']:
        elements.append(Paragraph(f"<b>{edu['degree']}</b>, {edu['institution']}", styles['Normal']))
        elements.append(Paragraph(edu['years'], styles['Italic']))
        elements.append(Spacer(1, 12))

    elements.append(Paragraph('Skills', styles['Heading2']))
    skills = ', '.join(data['skills'])
    elements.append(Paragraph(skills, styles['Normal']))
    elements.append(Spacer(1, 12))

    pdf.build(elements)
    messagebox.showinfo("Success", "Resume generated successfully!")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_data = get_user_input()
    generate_resume(user_data)

if __name__ == "__main__":
    main()

