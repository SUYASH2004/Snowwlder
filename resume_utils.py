"""Resume PDF parsing, normalization, and keyword extraction."""
import io
import re
from typing import List, Tuple
from pypdf import PdfReader


def extract_text_from_pdf(file_like) -> str:
    """Extract text from PDF (UploadedFile or bytes)."""
    if hasattr(file_like, "read"):
        data = file_like.read()
    elif isinstance(file_like, (bytes, bytearray)):
        data = file_like
    else:
        raise TypeError("Unsupported file input; expected UploadedFile or bytes.")

    reader = PdfReader(io.BytesIO(data))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def normalize_text(text: str) -> str:
    """Basic cleanup of extracted text."""
    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


_STOPWORDS = set(
    """
    a an the and or of in to for with on by at from up out as is are was were be been being
    this that those these i me my we our you your he she it they them their
    essential skills experience responsibilities requirements job role position
    """.split()
)


def top_keywords(text: str, k: int = 25) -> List[str]:
    """Lightweight keyword extractor."""
    tokens = re.findall(r"[a-zA-Z][a-zA-Z+.#\\-]{1,}", text.lower())
    freq = {}
    for t in tokens:
        if t in _STOPWORDS or len(t) < 2:
            continue
        freq[t] = freq.get(t, 0) + 1
    ranked = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [w for w, _ in ranked[:k]]


def keyword_overlap(resume_text: str, jd_text: str, k: int = 25) -> Tuple[List[str], List[str]]:
    """Return (matched, missing) keyword lists."""
    jd_keys = set(top_keywords(jd_text, k=k))
    res_keys = set(top_keywords(resume_text, k=2 * k))
    matched = sorted(list(jd_keys & res_keys))
    missing = sorted(list(jd_keys - res_keys))
    return matched, missing
