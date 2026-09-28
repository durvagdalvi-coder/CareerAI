from skill_engine import extract_skills



SKILL_WEIGHTS = {

    "fashion design": 5,
    "textile design": 4,
    "pattern making": 5,
    "illustrator": 4,
    "photoshop": 3,
    "trend forecasting": 3,
    "technical drawings": 3,


    "python": 5,
    "sql": 4,
    "api development": 4,
    "cloud": 4,
    "git": 2,


    "digital marketing": 5,
    "content strategy": 4,
    "social media": 3,
    "marketing analytics": 5,
    "seo": 3

}



def analyze_match(
    resume_text,
    job_text
):


    resume_skills = extract_skills(
        resume_text
    )


    job_skills = extract_skills(
        job_text
    )



    matched = []

    missing = []



    total_weight = 0

    matched_weight = 0



    for skill in job_skills:


        weight = SKILL_WEIGHTS.get(
            skill,
            1
        )


        total_weight += weight



        if skill in resume_skills:

            matched.append(
                skill
            )

            matched_weight += weight


        else:

            missing.append(
                skill
            )



    if total_weight > 0:

        score = int(
            (matched_weight / total_weight) * 100
        )

    else:

        score = 0



    return {

        "score": score,

        "matched": matched,

        "missing": missing,

        "required": job_skills

    }