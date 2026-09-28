import spacy
import re
from collections import Counter


nlp = spacy.load(
    "en_core_web_sm"
)


STOP_WORDS = {
    "experience",
    "years",
    "work",
    "working",
    "ability",
    "knowledge",
    "skills",
    "required",
    "preferred",
    "responsibilities",
    "role",
    "team",
    "company",
    "using"
}


SKILL_DATABASE = {

    "technology": [
        "python",
        "java",
        "sql",
        "javascript",
        "react",
        "django",
        "api",
        "aws",
        "docker",
        "cloud",
        "git"
    ],

    "marketing": [
        "seo",
        "content marketing",
        "digital marketing",
        "social media",
        "google analytics",
        "campaign management",
        "marketing analytics"
    ],

    "fashion": [
        "fashion design",
        "textile",
        "pattern making",
        "illustrator",
        "photoshop",
        "fabric selection",
        "trend forecasting",
        "technical drawing"
    ],

    "business": [
        "communication",
        "leadership",
        "project management",
        "strategy",
        "analysis"
    ]
}



def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    return text



def extract_keywords(text):

    cleaned = clean_text(text)


    doc = nlp(
        cleaned
    )


    keywords = []


    # NLP noun phrases

    for chunk in doc.noun_chunks:

        phrase = chunk.text.strip()


        if len(phrase.split()) <= 4:

            if phrase not in STOP_WORDS:

                keywords.append(
                    phrase
                )



    # Skill dictionary matching

    for category in SKILL_DATABASE.values():

        for skill in category:

            if skill in cleaned:

                keywords.append(
                    skill
                )



    # Frequency filtering

    counts = Counter(
        keywords
    )


    important = [

        word

        for word, count in counts.items()

        if count >= 1

    ]


    return list(
        set(important)
    )