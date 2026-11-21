"""Certificate Transparency collector via crt.sh (public)."""

from __future__ import annotations
from typing import Any, Dict, List
import requests

def collect_certificates(domain: str, timeout: int = 15) -> Dict[str, Any]:
    """
    Query crt.sh for certificates related to a domain.
    Passive and public.
    """
    url = f"https://crt.sh/?q={domain}&output=json"
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        # Deduplicate by name_value
        names = sorted({entry.get("name_value", "") for entry in data if entry.get("name_value")})
        return {
            "domain": domain,
            "source": "crt.sh",
            "certificate_count": len(data),
            "unique_names": names[:200],  # limit for safety
            "raw_count": len(data),
        }
    except Exception as e:
        return {
            "domain": domain,
            "source": "crt.sh",
            "error": str(e),
        }
