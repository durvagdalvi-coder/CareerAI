SKILL_LIBRARY = {


    "fashion": {

        "fashion design": [
            "fashion designer",
            "fashion design",
            "apparel design"
        ],

        "textile design": [
            "textile",
            "fabric",
            "textile design"
        ],

        "pattern making": [
            "pattern making",
            "pattern maker",
            "pattern development"
        ],

        "illustrator": [
            "adobe illustrator",
            "illustrator"
        ],

        "photoshop": [
            "adobe photoshop",
            "photoshop"
        ],

        "trend forecasting": [
            "trend forecasting",
            "fashion trends"
        ],

        "technical drawings": [
            "technical drawing",
            "fashion sketches"
        ]

    },


    "technology": {

        "python": [
            "python",
            "python programming"
        ],

        "sql": [
            "sql",
            "database"
        ],

        "api development": [
            "api",
            "rest api",
            "web services"
        ],

        "cloud": [
            "aws",
            "azure",
            "cloud computing"
        ],

        "git": [
            "git",
            "github",
            "version control"
        ]

    },


    "marketing": {

        "digital marketing": [
            "digital marketing",
            "online marketing"
        ],

        "content strategy": [
            "content strategy",
            "content planning"
        ],

        "social media": [
            "social media",
            "social platforms"
        ],

        "marketing analytics": [
            "marketing analytics",
            "campaign metrics",
            "performance analysis"
        ],

        "seo": [
            "seo",
            "search engine optimization"
        ]

    }

}



def extract_skills(text):

    text = text.lower()


    found = []


    for category in SKILL_LIBRARY.values():

        for skill, synonyms in category.items():

            for word in synonyms:

                if word in text:

                    found.append(skill)

                    break



    return list(set(found))