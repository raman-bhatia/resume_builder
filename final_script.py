import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

os.environ["OPENAI_API_KEY"] = "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"

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
def create_resume():

    # %%
    print("Welcome to the Resume Generator")
    print("================================")
    print("Provide job type either SWE or TPM")
    
    job_type = input()

    # %%
    print("Enter/Paste job description. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    job_description = """ Job Description: """
    while True:
        try:
            line = input()
        except EOFError:
            break
        job_description.join(line)

    print("Wait..... The AI is on work, creating your beautiful resume...")
    # %%
    my_skills = ["Python", "Java", "C", "C++", "SQL", "Git", "VM",
    "Non-Relational Databases", "No SQL", "CI/CD", "APIs",
    "Django", "ReactJS", "NodeJS", "Unix", "Linux", "Windows", "Jira", "Confluence", "Google Suite", "Office 365", "ChatGPT",
    "Java Script", "GitLab"]

    # %%
    my_education = """
    Masters in Computer Science (MCIT)
    University of Pennsylvania, Philadelphia, PA, Dec 2022
    Specialization: Artificial Intelligence and Data Engineering

    Master of Business Administration (MBA)
    Winston Salem State University, Winston Salem, NC, Dec 2010
    Specialization: Economics and Finance

    Bachelor in Science (BSc)
    Indira Gandhi National University, New Delhi, India, Jun 2010
    Specialization: Mathematics
    """

    # %%
    my_contact = """
    Ramanpreet Bhatia
    Fremont, CA 
    (661) 447-0720
    i.raman.bhatia@gmail.com
    linkedin.com/in/ramanpreetbhatia/
    github.com/raman-bhatia
    """

    work_authorization = "Green Card | Able to work in the US without sponsorship"

    # %%
    my_experience = """Hello"""
    if job_type == "TPM":
        my_experience = """
        Workday Inc, Pleasanton, CA
        Software Application Engineer Sept 2021 - Present
        - Develop financial application using Object-Oriented Programming techniques.
        - Developed APIs for testing to make HTTP requests and simulate responses when the
        backend Machine Learning model was unavailable.
        - Conduct unit tests to ensure high-quality software and create automation scripts for feature
        testing and end-to-end release testing.
        - Participate in agile development process and collaborate on code reviews and stories.
        - Develop and maintain CI/CD scripts and infrastructure, ensuring continuous integration and
        delivery of high-quality software releases.
        
        University of Pennsylvania, Philadelphia, PA
        Graduate Student Aug 2019 - Dec 2022
        - Key courses: - Introduction to Software Development, Mathematical Foundation of Computer
        Science, Algorithms and Computation, Data Structures and Software Design, Introduction to
        Computer Systems, Computer Systems Programming, Statistics for Data Science, Enterprise
        Data Management, Big Data Analytics, Blockchains and Cryptography
        - Designed & developed apps using OOP, DRY, unit testing, data modeling, architecture, and
        publicly available data. Utilized AWS computing environment for multiple projects.
        
        IQVIA, McKesson, Verizon, Highmark, CareSource, Houston, TX
        Technical Project Manager Aug 2011 - Feb 2019
        - Experienced IT project management consultant in Software and Data Engineering Teams, having worked for reputed companies, having
        led cross-functional teams and also performed quantitative and qualitative analysis to ensure
        data quality using SQL, Python, and Excel Pivot tables.
        - Demonstrated experience in product management, with a track record of serving as a product
        portfolio manager for 3 in-house applications and contributing innovative ideas to implement
        rigorous best practices processes for digital platforms across the organization.
        - Proficient in Agile and Scrum methodologies, having conducted sprint reviews and initiated
        daily stand-ups with leads and team members to identify and mitigate blockers/challenges.
        - Skilled in budgeting, having developed project plans for multiple projects with a budget of up
        to $2M, based on charter, PRDs, and other inputs, ensuring mutual agreement, culminating in
        the successful completion of the projects.
        - Proven track record of leading more than 15 different technology-focused projects in a
        multi-tier Agile development environment, adhering to PMO established standards, and acting
        as a liaison for development and maintenance of different applications within HL7
        (ANSI accredited), HIPAA, HCP, and CMS guidelines.

        """
    elif job_type == "SWE":
        my_experience = """
        Workday Inc, Pleasanton, CA
        Software Application Engineer Sept 2021 - Present
        - Developed financial application using Java and OOP techniques.
        - Developed APIs for testing to make HTTP requests and simulate responses when
        the backend Machine Learning model is unavailable using Python FastAPI.
        - Conduct unit tests to ensure high-quality software and create automation scripts
        for feature testing and end-to-end release testing
        - Participate in agile development process and collaborate on code reviews,
        knowledge sharing, and mentoring.
        - Developed and maintained CI/CD scripts ensuring continuous integration and
        delivery of high-quality software releases using dockers & shell scripts.
        Helpsy Health, San Jose, CA
        Software Quality Intern May 2020 - Aug 2020
        - Worked with development team to diagnose and fix app bugs.
        - Created project plan covering budget, release cycle, sprints, etc.
        University of Pennsylvania, Philadelphia, PA
        Graduate Student Aug 2019 - Dec 2022
        - Designed & developed apps using OOP, unit testing, data modeling, architecture,
        and publicly available data. Used AWS computer environment, MySQL.
        - Executed data cleansing, loading, and query optimization.
        - Built minimalist UIs for the projects in a collaborative environment..
        - Built apps using DRY, CRC & OOD principles.
        - Leveraged Git to maintain the code and collaborate with team members
        IQVIA, McKesson, Verizon, Highmark, CareSource, Houston, TX
        Technical Project Manager Aug 2011 - Feb 2019
        - Consulted as IT project manager for healthcare and tech firms.
        - Led data curation and engineering teams with daily SCRUM standups.
        - Gathered customer requirements and managed applications as portfolio manager.
        Improved SDLC processes and drove best practices.
        - Developed and executed project plans with $2M budget.
        """
    else:
        raise ValueError("Provide job type as SWE or TPM")

    # %%
    my_projects = """

    Hospital Ranking App
    University of Pennsylvania
    Designed & developed hospital ranking app
    using OOP, unit testing, data modeling,
    architecture & publicly available data using
    Python. Built a minimalist UI using ReactJS.

    Nearby Recommendation App
    University of Pennsylvania
    Developed recommendation app for restaurants,
    schools, crime, population & income using AWS,
    MySQL, ReactJS. Included data cleansing,
    loading, and query optimization.

    Healthy Food App
    University of Pennsylvania
    Developed a CLI based app to search for
    healthy products utilizing the large OpenFood
    database using AWS computing env.

    Spell Checker App
    University of Pennsylvania
    Developed games and apps in Java using
    DRY, CRC & OOD principles.

    Cross-Validation in Machine Learning
    Medium
    Published article on application of
    cross-validation in machine learning. This
    publication has >6.5 views.

    """

    # %%
    my_certifications = """
    Project Management Professional (PMP), PMI
    License #: 1775635 2014-2023
    Certified Scrum Master (CSM), Scrum Alliance
    License # 1019888 2019 - 2023
    """

    # %%
    prompt = f"""
        Your task is to create a tailored resume for the provided job description.

        Here is the job description: ```{job_description}```

        Here are parts of my profile:
        My technical skills:  ```{my_skills}```. 
        My education: ```{my_education}```. 
        My contact information: ```{my_contact}```. 
        My experience: ```{my_experience}```.
        My projects: ```{my_projects}```. 
        My certifications: ```{my_certifications}```. 
        My work authorization: ```{work_authorization}```.

        Additional instructions are as follows:

        - Write short executive summary based on my profile that matches the job description as much as possible.

        - Review the experience section and make is shorter that is best match to the job description.

        - Dont mention if you wrote it.

        - Create the resume in the html page of A4 size with two columns with total width of 100% and right column width of 34% width.

        - Use professional font with compact spacing and style with 8pt font size for text and 10pt font size for h2 and 12pt for h1.

        - Put executive summary, my experience, and my education in the first column

        - Put my skills, my projects with brief details, and my certifications in the second column.

        - Put best matched skills as buttons in horizontal manner but keep them under 10 in count.

        - Dont put skills in the executive summary that are not in the job description.

        - Dont use any job description parts in the resume.

        - Put my name and contact information in the header and my work authorization status in the footer and center them.

    """

    # %%
    response = get_completion(prompt)
    with open('index.html', 'w') as f:
        f.write(response)
        
    print("Done : Check index.html file for output")
        
    return response

if __name__ == '__main__':
    create_resume()

    # %%



