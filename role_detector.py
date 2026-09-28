def detect_role(job_text):

    text = job_text.lower()


    role_patterns = {


        "Fashion Designer": {

            "industry": "Fashion & Creative Design",

            "keywords": [
                "fashion",
                "textile",
                "pattern",
                "garment",
                "apparel",
                "illustrator",
                "fabric"
            ]

        },


        "Software Developer": {

            "industry": "Technology",

            "keywords": [
                "python",
                "java",
                "software",
                "developer",
                "api",
                "database",
                "coding",
                "programming"
            ]

        },


        "Data Analyst": {

            "industry": "Data & Analytics",

            "keywords": [
                "data",
                "analytics",
                "sql",
                "excel",
                "dashboard",
                "statistics"
            ]

        },


        "AI Marketing Specialist": {

            "industry": "Marketing",

            "keywords": [
                "marketing",
                "campaign",
                "social media",
                "content",
                "seo",
                "analytics"
            ]

        },


        "HR Specialist": {

            "industry": "Human Resources",

            "keywords": [
                "recruitment",
                "hiring",
                "employee",
                "hr",
                "talent"
            ]

        }

    }



    scores = {}


    for role, data in role_patterns.items():

        score = 0


        for keyword in data["keywords"]:

            if keyword in text:

                score += 1


        scores[role] = score



    detected_role = max(
        scores,
        key=scores.get
    )


    if scores[detected_role] == 0:

        return {

            "role": "General Professional Role",

            "industry": "Not Classified"

        }



    return {

        "role": detected_role,

        "industry": role_patterns[detected_role]["industry"]

    }