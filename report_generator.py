def generate_cover_letter(
    matched_skills,
    job_title="AI Marketing Specialist"
):

    skills = ", ".join(
        matched_skills
    )


    cover_letter = f"""
Dear Hiring Manager,

I am interested in the {job_title} position.
My experience with {skills} aligns with the
requirements of this role.

I have developed skills in technology,
creative problem solving, and digital workflows.
I am interested in applying these capabilities
to create impactful marketing solutions.

I would appreciate the opportunity to discuss
how my skills can contribute to your team.

Sincerely,
Candidate
"""

    return cover_letter



def generate_report(
    score,
    matched,
    missing,
    suggestions,
    summary,
    questions
):

    report = f"""

==================================
CareerAI Resume Analysis Report
==================================


ATS Compatibility Score:

{score}%



==================================
Matched Skills
==================================

"""


    for skill in matched:

        report += f"✓ {skill}\n"



    report += """

==================================
Skill Gaps
==================================

"""


    for skill in missing:

        report += f"• {skill}\n"



    report += """

==================================
Resume Improvement Suggestions
==================================

"""


    for suggestion in suggestions:

        report += f"→ {suggestion}\n"



    report += """

==================================
Professional Summary
==================================

"""


    report += summary



    report += """

==================================
Cover Letter
==================================

"""


    report += generate_cover_letter(
        matched
    )



    report += """

==================================
Interview Questions
==================================

"""


    for question in questions:

        report += f"• {question}\n"



    return report