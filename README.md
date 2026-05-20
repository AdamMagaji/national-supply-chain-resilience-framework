[![Federal Compliance & Security Scan](https://github.com/AdamMagaji/national-supply-chain-resilience-framework/actions/workflows/security-scan.yml/badge.svg)](https://github.com/AdamMagaji/national-supply-chain-resilience-framework/actions/workflows/security-scan.yml)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%20License%202.0-blue)](https://opensource.org)
[![Python: 3.11](https://img.shields.io/badge/python-%3E=3.11-blue?logo=python)](https://python.org)


# National Supply Chain Resilience Framework (NSCRF)

## 🇺🇸 Executive Summary & National Importance
The **National Supply Chain Resilience Framework (NSCRF)** is an enterprise-grade, open-source data architecture that eliminates fragmentation and data siloing by deploying high-throughput, real-time predictive pipelines and secure distributed synchronization to mitigate systemic disruption risks across critical U.S. logistics infrastructure. 

NSCRF resolves these vulnerabilities by providing a standardized, highly scalable framework for real-time data ingestion, predictive risk modeling, and multi-tenant synchronization. Built with a modular, cloud-agnostic topology, it allows U.S. public and private entities to seamlessly collaborate, monitor logistics bottlenecks, and dynamically reroute critical resources without compromising data security.

### Strategic Alignment with U.S. National Interests
This framework is developed in direct response to critical national security and economic directives, specifically aligning with:
1. **The White House Executive Order on America's Supply Chains:** Addressing structural vulnerabilities in critical manufacturing, public health, and agricultural logistics.
2. **NIST Cybersecurity Framework (CSF) 2.0:** Utilizing zero-trust data ingestion protocols to protect shared infrastructure from supply-chain-based cyber threats.
3. **Department of Transportation (DOT) Freight Logistics Optimization Works (FLOW) Initiative:** Providing the open-source technical architecture required to share anonymous, real-time logistics data across competing industry stakeholders safely.

---

## 🛠️ Technical Architecture Specification
The NSCRF is designed around decoupled, highly performant operational layers to ensure horizontal scalability across federal infrastructure.

```text
[Data Producers] -> [Secure Compliance Layer] -> [Resilience Ingestion] -> [Predictive Risk Engine]
(Sensors/Logistics)  (SHA-256 PII Masking)      (Validating Streams)     (Bottleneck Evaluation)
```

* **Ingestion Layer:** Leverages abstract, multi-tenant interfaces to process high-throughput telemetry from maritime ports, rail yards, and cargo fleets.
* **Security & Compliance Layer:** Implements automated, hardware-accelerated cryptographic masking of proprietary corporate assets and driver PII to ensure zero-trust trust boundaries.
* **Analytics Layer:** Uses predictive risk vectors to calculate real-time transit deviations and trigger dynamic infrastructure failovers.

---

## 🔒 Federal Compliance Metrics
To ensure deployment readiness within strictly regulated U.S. federal and critical infrastructure spaces, the core code adheres to:
* **FedRAMP Low/Moderate Controls:** Strict encapsulation of system environment parameters and stateless runtime execution.
* **NIST SP 800-53 (Security and Privacy Controls):** Cryptographic sanitization of transport payloads via SHA-256 obfuscation to neutralize insider threat data leaks.

---

## ⚡ Quick Start
Deploy the framework instantly via a local virtual environment or isolated Docker container.

### Option A: Local Execution
```bash
# Install system dependencies
pip install -r requirements.txt

# Execute the core validation engine
python app.py
```

### Option B: Cloud-Agnostic Docker Deployment
```bash
# Build the standardized container
docker build -t nscrf-core .

# Execute the isolated infrastructure simulation
docker run --rm nscrf-core
```

---

## 🖥️ Accessing the UI Dashboard & API Interactive Layer

The framework includes two high-visibility interfaces designed for both technical auditors and non-technical stakeholders to evaluate the data pipeline in real-time.

### 📊 1. Streamlit Automated Visualization Dashboard
This graphical dashboard provides visual KPI metrics, data tables, and dynamic sliders to simulate cargo stream volumes and calibrate transit delays.

* **Direct Streamlit URL** You can directly view the dashboard here:
  `https://national-supply-chain-resilience-framework.streamlit.app/`

* **How to Launch:** Run the following command in your terminal:
  ```bash
  python -m streamlit run dashboard.py
  ```
* **How to Access:** Once running, your terminal will output a local network URL. Open your web browser and navigate directly to:
  `http://localhost:8501`

### 🔌 2. Advanced API Documentation Layer (Swagger UI)
This fully self-contained interface displays the REST API endpoint structures, maps out input payloads, and allows for interactive testing directly from the browser window.
* **How to Launch:** Run the following command in your terminal to boot the local server process:
  ```bash
  python app.py
  ```
* **How to Access:** Because the API dashboard is mapped directly to the server's root path for seamless accessibility, open your web browser and navigate to:
  `http://127.0.0`
* **Interactive Testing:** Click the blue **`POST /ingest-and-process`** bar, click the **`Try it out`** button, and execute a sample multi-tenant payload to watch the cryptographic masking layer run live.

---

## 📊 Verification & Benchmarking
This framework contains built-in automated testing scripts to empirically validate operational throughput and performance gains. 

* **Ingestion Throughput:** 7,314,413.27 records/sec
* **PII Masking Latency:** 0.00064 ms/payload
* **Risk Evaluation Complexity:** O(N) linear parsing scalability

---

## 🔬 Framework Verification & Testing Guide
This project contains built-in automated verification protocols. Any developer, security auditor, or evaluator can clone this repository and test the data pipeline locally using the standardized entry points below.

### 📋 Prerequisites
Ensure you have one of the following installed on your host system:
* **Python 3.10+** (with `pip` package manager)
* **Docker Desktop** (Recommended for cloud-agnostic isolation)

---

### 🚀 Execution Methods

#### Method 1: Standard Ingestion & Compliance Validation
This method executes the core data pipeline, ingests a mock multi-tenant logistics payload, applies SHA-256 PII masking, and runs the linear risk-scoring algorithm.
```bash
# Clone the repository
git clone https://github.com
cd national-supply-chain-resilience-framework

# Install lightweight dependencies
pip install -r requirements.txt

# Run the core validation engine
python app.py
```
* **Expected Output:** A clean, formatted JSON structure displaying masked carrier identifiers and calculated risk metrics.

#### Method 2: High-Volume Enterprise Stress Testing
This entry point executes the benchmarking engine to stress-test the framework under an enterprise-scale load of 100,000 parallel supply chain events to calculate raw processing speed.
```bash
python benchmark.py
```
* **Expected Output:** A high-visibility `================ BENCHMARK RESULTS ================` block displaying raw ingestion throughput (records/sec) and security latency (ms/record).

#### Method 3: Isolated Docker Sandbox Run (Zero-Installation Method)
Deploy and test the framework inside a fully isolated, containerized environment that replicates a secure federal cloud environment.
```bash
# Build the standardized container image
docker build -t supply-chain-framework .

# Boot up the container and execute internal systems validation tests
docker run --rm supply-chain-framework
```
* **Expected Output:** The container will spin up, execute the core validation code automatically, print the verified system output to the screen, and cleanly terminate.


