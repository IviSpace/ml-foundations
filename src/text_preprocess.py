import re

URL_RE = re.compile(r"https?://\S+|www\.\S+")
HTML_RE = re.compile(r"<.*?>")
NON_ALPHA_RE = re.compile(r"[^a-zA-Z\s]")

def clean_text(
    text: str,
    lowercase: bool = True,
    remove_urls: bool = True,
    remove_html: bool = True,
    remove_non_alpha: bool = True,
    collapse_spaces: bool = True,
     
) -> str:

    """
     Minimal, fast cleaning for classic ML vectorizers (Count/TF-IDF).

    Why this exists:
    - Vectorizers treat different strings as different features.
    - Cleaning improves consistency (e.g., 'Great!' vs 'great').
    """
    
    if text is None:
        return ""

    t = text
#Don’t interpret backslashes — pass them to regex as-is.”
    if remove_urls :
        t = re.sub(URL_RE, " ", t)
        print(t)
    if remove_html :
        t= re.sub(HTML_RE, " ", t)
        print(t)
    if lowercase :
        t = t.lower()
        print(t)
    if remove_non_alpha :
        t = re.sub(NON_ALPHA_RE, " ", t)
        print(t)
    if collapse_spaces :
        t = re.sub(r"\s+", " ", t).strip()
        print(t)
    return t
