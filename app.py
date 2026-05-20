from fastapi_offline import FastAPIOffline
from typing import List, Dict, Any
from core.pipeline import ResiliencePipeline
from core.security import SecureComplianceLayer
import uvicorn

# Initialize the API with the main documentation endpoint forced onto the ROOT path (/)
app = FastAPIOffline(
    title="National Supply Chain Resilience Framework (NSCRF) API",
    description="Federal-ready REST API architecture designed for real-time logistics data ingestion, NIST-compliant PII masking, and linear risk vector assessment.",
    version="1.0.0",
    docs_url="/"  # Forces the visual dashboard to open instantly on the main page
)

@app.post("/ingest-and-process", response_model=List[Dict[str, Any]])
def process_supply_chain_stream(payload: List[Dict[str, Any]]):
    """
    Ingests raw multi-tenant supply chain telemetry, applies cryptographic privacy masks 
    to carrier identifiers, and maps real-time logistics bottlenecks.
    """
    pipeline = ResiliencePipeline(pipeline_id="NSCRF-API-NODE-01")
    compliance = SecureComplianceLayer()
    
    secured_data = compliance.mask_pii(payload, target_fields=["carrier_name"])
    processed_results = pipeline.evaluate_risk(secured_data)
    
    return processed_results

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)
