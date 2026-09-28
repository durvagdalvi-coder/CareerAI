def generate_suggestions(
    missing_skills,
    role="General Professional Role"
):


    suggestion_database = {


        "fashion designer": {


            "pattern making":
            "Add garment construction projects, pattern development examples, or portfolio work demonstrating design skills.",


            "textile design":
            "Highlight fabric knowledge, textile selection, material research, and experimentation.",


            "illustrator":
            "Include Adobe Illustrator experience and examples of digital fashion sketches.",


            "photoshop":
            "Mention visual editing, fashion boards, and creative design workflows.",


            "trend forecasting":
            "Add examples of fashion research, trend analysis, and market observation."

        },



        "software developer": {


            "python":
            "Add Python projects, automation scripts, or backend development examples.",


            "sql":
            "Highlight database projects, queries, reporting, or data management experience.",


            "api development":
            "Include API projects, integrations, or backend service development.",


            "cloud":
            "Add cloud deployment experience using platforms such as AWS or Azure.",


            "git":
            "Mention version control workflows and collaborative development practices."

        },



        "ai marketing specialist": {


            "digital marketing":
            "Add examples of campaigns, online marketing activities, and audience growth initiatives.",


            "marketing analytics":
            "Highlight campaign metrics, reporting, analytics tools, and performance tracking.",


            "seo":
            "Include search optimization activities and content visibility improvements.",


            "social media":
            "Add social media strategy, content calendars, and engagement results."

        }

    }



    role_key = role.lower()


    suggestions = []



    for skill in missing_skills:


        found = False


        for category, skills in suggestion_database.items():


            if category in role_key:


                if skill in skills:

                    suggestions.append(
                        skills[skill]
                    )

                    found = True



        if not found:

            suggestions.append(
                f"Consider adding projects or experience that demonstrate {skill} capability."
            )



    return suggestions





def generate_summary(
    matched_skills
):


    skills = ", ".join(
        matched_skills
    )


    return f"""
Professional with experience in {skills}.
Able to apply technical knowledge,
problem solving, and role-specific skills
to deliver effective results.
"""





def generate_questions(
    job_title="target role"
):


    return [

        f"Explain your experience related to the {job_title} role.",

        "Describe a project where you applied your professional skills.",

        "How do you continue improving your industry knowledge?",

        "Describe a challenge you solved in your previous work.",

        "How would you contribute to this role?"

    ]