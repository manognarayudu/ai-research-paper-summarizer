from transformers import pipeline

# Load summarization model ONCE
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def generate_summary(text):
    """
    This function takes long text
    and returns a short summary
    """

    # Safety: limit text size (AI models have limits)
    if len(text) > 3000:
        text = text[:3000]

    summary = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]
