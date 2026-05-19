from core.pipeline import ResiliencePipeline
from core.security import SecureComplianceLayer
import json

def run_framework_demo():
    # 1. Mock Critical Supply Chain Payload (e.g., Medical Supplies or Semiconductor Logistics)
    mock_logistics_data = [
        {"shipment_id": "SHIP-9081", "carrier_name": "GlobalTransitCorp", "transit_delay_days": 6, "destination_hub": "Port of Los Angeles"},
        {"shipment_id": "SHIP-1102", "carrier_name": "ApexLogisticsLtd", "transit_delay_days": 2, "destination_hub": "Chicago O'Hare"}
    ]
    
    # 2. Instantiate Architecture
    pipeline = ResiliencePipeline(pipeline_id="NSCRF-US-WEST-01")
    compliance = SecureComplianceLayer()
    
    # 3. Secure data layer (Masking sensitive carrier data to protect trade secrets)
    secured_data = compliance.mask_pii(mock_logistics_data, target_fields=["carrier_name"])
    
    # 4. Ingest and Process risk metrics
    ingested_data = pipeline.ingest_batch(secured_data)
    processed_results = pipeline.evaluate_risk(ingested_data)
    
    # Print results to demonstrate framework utility
    print("\n--- PROCESSED COMPLIANT SYSTEM OUTPUT ---")
    print(json.dumps(processed_results, indent=4))

if __name__ == "__main__":
    run_framework_demo()
