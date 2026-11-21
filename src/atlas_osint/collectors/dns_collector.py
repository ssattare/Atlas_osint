"""Passive DNS collector using dnspython."""

from __future__ import annotations
from typing import Dict, List, Any

try:
    import dns.resolver
    HAS_DNSPYTHON = True
except ImportError:
    HAS_DNSPYTHON = False


def collect_dns(domain: str, record_types: List[str] | None = None) -> Dict[str, Any]:
    """
    Collect common DNS records for a domain.
    Returns a dict suitable for later conversion to Evidence records.
    """
    if not HAS_DNSPYTHON:
        return {"error": "dnspython not installed", "domain": domain}

    if record_types is None:
        record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    results: Dict[str, Any] = {
        "domain": domain,
        "records": {},
        "errors": {},
    }

    resolver = dns.resolver.Resolver()
    resolver.lifetime = 5.0

    for rtype in record_types:
        try:
            answers = resolver.resolve(domain, rtype)
            results["records"][rtype] = [r.to_text() for r in answers]
        except Exception as e:
            results["errors"][rtype] = str(e)

    return results
