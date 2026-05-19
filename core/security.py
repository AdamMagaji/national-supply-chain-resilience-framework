import hashlib
from typing import Dict, Any, List

class SecureComplianceLayer:
    """Provides automated data anonymization to meet NIST and FedRAMP security standards."""
    
    def __init__(self, salt: str = "USCRF_SECURE_SALT_2026"):
        self.salt = salt

    def mask_pii(self, records: List[Dict[str, Any]], target_fields: List[str]) -> List[Dict[str, Any]]:
        """Anonymizes proprietary supply chain details or vendor PII using SHA-256."""
        for record in records:
            for field in target_fields:
                if field in record and record[field]:
                    raw_value = str(record[field]) + self.salt
                    record[field] = hashlib.sha256(raw_value.encode()).hexdigest()[:16]
        return records
