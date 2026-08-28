# Specula

## Threat Intelligence Monitoring & IOC Correlation Platform

---

## 1. Project Overview

Specula is a threat intelligence platform designed to collect, normalize,
correlate, and monitor Indicators of Compromise (IoCs) from multiple
threat intelligence sources.

The platform provides a centralized view of threat intelligence data
and allows security analysts to investigate IoCs through a web interface
and REST API.

Specula combines normalized IOC information with source-specific intelligence,
allowing information from different providers to be correlated while preserving the original data returned by each source.
---

## 2. Problem Statement

Threat intelligence data is distributed across multiple external sources.
Security analysts may need to manually check several sources to determine
the reputation and context of an Indicator of Compromise.

Specula aims to centralize this information and provide a unified view
of IoCs collected from multiple threat intelligence sources.

---

## 3. Project Goals

- Collect IoCs from multiple threat intelligence sources
- Normalize data received from different sources
- Detect and remove duplicate IoCs
- Correlate information from multiple sources
- Monitor changes in IoC reputation
- Provide a unified risk/reputation overview
- Store historical threat intelligence data
- Provide a web interface for security analysts
- Expose threat intelligence through a REST API 
- Preserve source-specific threat intelligence
- Store raw provider responses for further investigation
- Calculate an aggregated risk assessment based on available intelligence
- Support investigation of file-related behavioural intelligence
- Design the system so that additional intelligence sources can be integrated later

---

## 4. Supported IoC Types

Initial IoC types:

- IPv4 addresses
- IPv6 addresses
- Domains
- URLs
- Files/ File hashes

File intelligence may include multiple hash representations such as:

- MD5
- SHA-1
- SHA-256
- TLSH
- VHASH
- Permhash
---

## 5. Core Features

### MVP

- IoC lookup
- Threat feed ingestion
- Data normalization
- IoC deduplication
- Source-specific intelligence storage
- Raw JSON response preservation
- Basic risk assessment
- Multi-source correlation
- Aggregated risk assessment
- Historical observation storage
- File intelligence lookup
- File behaviour analysis
- REST API
- Basic web dashboard

### Future Features

- Automated alerts
- Background processing
- STIX 2.1 support
- TAXII integration
- SIEM integration
- Authentication and authorization

---

## 6. Threat Intelligence Sources

Initial sources:

- VirusTotal
- AbuseIPDB
- AlienVault OTX

The platform should be designed so that additional sources
can be integrated later.

### VirusTotal

VirusTotal provides intelligence for multiple IOC types, including IP addresses, domains, URLs, and files.

Depending on the IOC type, VirusTotal may provide:

* Reputation and analysis statistics
* Security engine detections
* Tags
* Network and DNS information
* WHOIS information
* File metadata
* Sandbox verdicts
* Malware-related information
* File behaviour
* MITRE ATT&CK techniques

### AbuseIPDB

AbuseIPDB focuses primarily on IP address reputation and abuse reporting.

Relevant information may include:

* IP address
* IP version
* Abuse confidence score
* Country
* ISP
* Domain
* Usage type
* Hostnames
* Tor status
* Number of reports
* Reporter information
* Last reported time
* Abuse categories

### AlienVault OTX

AlienVault OTX organizes threat intelligence through Pulses and Indicators.

OTX may provide:

* Indicator information
* Pulse information
* Threat context
* Tags
* Malware families
* Adversary information
* MITRE ATT&CK references
* References and other source-specific metadata

---

## 7. High-Level Data Flow

Threat Intelligence Sources
        ↓
Data Ingestion
        ↓
Normalization
        ↓
Deduplication
        ↓
Correlation
        ↓
Risk Assessment
        ↓
Database
        ↓
Dashboard / REST API

---

## 8. Technology Stack

### Backend
- Python
- FastAPI

### Database
- PostgreSQL
- SQLAlchemy

### Background Processing
- Celery
- Redis

### Frontend
- HTML
- Bootstrap
- Jinja2
- Chart.js

### Infrastructure
- Docker
- Docker Compose

### Testing
- pytest

### CI/CD
- GitHub Actions

---

## 9. Project Scope

The initial version of Specula focuses on collecting, storing, normalizing, and correlating threat intelligence from multiple external providers.

Specula does not independently discover malicious activity and does not replace dedicated security products such as antivirus, EDR, SIEM, or malware analysis platforms.

Instead, it aggregates intelligence provided by external sources and presents it in a centralized form for security investigation.

The aggregated risk assessment is intended as an analytical aid and should not be interpreted as a definitive verdict without further investigation.

---

## 10. Future Improvements

- Elasticsearch for large-scale IOC search
- Advanced correlation rules
- Automated alerting
- SIEM integrations
- STIX/TAXII support
- User authentication
- Role-based access control
- Cloud deployment

## Data Model Strategy

Specula stores threat intelligence on two levels:

1. **Normalized IOC records** – common attributes shared across all threat intelligence sources.
2. **Source observations** – source-specific metadata and raw intelligence data returned by individual providers.

This architecture allows correlation, historical tracking, risk score recalculation, and integration of additional threat intelligence sources without modifying the core IOC model.

## Target Users

### Security Analyst

The primary user of Specula. Security analysts use the platform to search, investigate, and monitor Indicators of Compromise collected from multiple threat intelligence sources.

### Security Tools

External security systems (SIEM, SOAR, firewalls, or internal security tools) can query Specula through the REST API to retrieve reputation and contextual information about known IoCs.

