import marvin


def extract_subject(question):
    subject = marvin.extract(
        question,
        instructions="From the question: {{ question }}, extract the main subject. Limit to 1. Use temperature=0",
    )
    return subject


@marvin.fn
def python_framework_recommendation(extracted_subject: str):
    """Recommend the most suitable Python framework or Module based on {{ extracted_subject }}. Just return the framework."""


# Natural Language Generation
@marvin.fn
def generate_nl(input: str):
    """With {{ input }}, rewrite sentence with correct grammar, punctuation and sentence structure. Remove any symbols, for example brackets and quotes that are not needed in a regular english sentence."""
