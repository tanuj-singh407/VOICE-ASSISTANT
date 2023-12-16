from fpdf import FPDF

class Resume:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""
        self.summary = ""
        self.skills = []
        self.experience = []
        self.education = []

    def set_basic_info(self):
        print("Enter your basic information:")
        self.name = input("Full Name: ")
        self.email = input("Email: ")
        self.phone = input("Phone: ")

    def set_summary(self):
        print("\nEnter a brief summary about yourself:")
        self.summary = input()

    def add_skill(self):
        skill = input("Enter a skill: ")
        self.skills.append(skill)

    def add_experience(self):
        print("\nEnter your work experience (Enter 'q' to quit):")
        while True:
            company = input("Company/Organization: ")
            if company.lower() == 'q':
                break
            title = input("Job Title: ")
            duration = input("Duration: ")
            description = input("Description: ")

            experience = {
                "company": company,
                "title": title,
                "duration": duration,
                "description": description
            }
            self.experience.append(experience)

    def add_education(self):
        print("\nEnter your education details (Enter 'q' to quit):")
        while True:
            degree = input("Degree: ")
            if degree.lower() == 'q':
                break
            university = input("University/Institution: ")
            year = input("Year: ")

            education = {
                "degree": degree,
                "university": university,
                "year": year
            }
            self.education.append(education)

    def generate_text_resume(self):
        print("\n---------- Resume ----------")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}\n")
        print(f"Summary: {self.summary}\n")
        print("Skills:")
        for skill in self.skills:
            print(f"- {skill}")
        print("\nExperience:")
        for exp in self.experience:
            print(f"- {exp['title']} at {exp['company']} ({exp['duration']})")
            print(f"  {exp['description']}")
        print("\nEducation:")
        for edu in self.education:
            print(f"- {edu['degree']} from {edu['university']} ({edu['year']})")

    def generate_pdf_resume(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Set resume title
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Resume", ln=True, align="C")

        # Add basic info
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Basic Information", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Name: {self.name}", ln=True)
        pdf.cell(0, 10, f"Email: {self.email}", ln=True)
        pdf.cell(0, 10, f"Phone: {self.phone}", ln=True)

        # Add summary
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Summary", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, self.summary)

        # Add skills
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Skills", ln=True)
        pdf.set_font("Arial", "", 12)
        for skill in self.skills:
            pdf.cell(0, 10, f"- {skill}", ln=True)

        # Add experience
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Experience", ln=True)
        pdf.set_font("Arial", "", 12)
        for exp in self.experience:
            pdf.cell(0, 10, f"- {exp['title']} at {exp['company']} ({exp['duration']})", ln=True)
            pdf.multi_cell(0, 10, exp['description'])

        # Add education
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Education", ln=True)
        pdf.set_font("Arial", "", 12)
        for edu in self.education:
            pdf.cell(0, 10, f"- {edu['degree']} from {edu['university']} ({edu['year']})", ln=True)

        pdf.output("resume.pdf")

    def generate_resume(self):
        self.set_basic_info()
        self.set_summary()

        print("\nEnter your skills (Enter 'q' to quit):")
        while True:
            skill = input("Enter a skill: ")
            if skill.lower() == 'q':
                break
            self.skills.append(skill)

        self.add_experience()
        self.add_education()

        self.generate_text_resume()
        self.generate_pdf_resume()

def main():
    resume = Resume()
    resume.generate_resume()

if __name__ == "__main__":
    main()
