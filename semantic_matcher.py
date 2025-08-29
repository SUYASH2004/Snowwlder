"""Compute resume–JD similarity score using embeddings + keyword overlap."""
from typing import Dict, Any

from gemini_utils import embed_text, cosine_sim
from resume_utils import normalize_text, keyword_overlap


def compute_match(resume_text: str, jd_text: str) -> Dict[str, Any]:
    resume_clean = normalize_text(resume_text)
    jd_clean = normalize_text(jd_text)

    # Embedding similarity
    e_resume = embed_text(resume_clean[:18000])
    e_jd = embed_text(jd_clean[:8000])
    emb_sim = cosine_sim(e_resume, e_jd)

    # Keyword overlap
    matched, missing = keyword_overlap(resume_clean, jd_clean, k=25)
    if (len(matched) + len(missing)) == 0:
        kw_score = 0.0
    else:
        kw_score = len(matched) / (len(matched) + len(missing))

    # Weighted final score
    final_score = 0.7 * emb_sim + 0.3 * kw_score

    return {
        "embedding_similarity": round(emb_sim, 4),
        "keyword_score": round(kw_score, 4),
        "final_score": round(final_score, 4),
        "matched_keywords": matched,
        "missing_keywords": missing,
    }
