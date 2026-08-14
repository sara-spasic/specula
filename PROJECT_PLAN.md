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

---

## 4. Supported IoC Types

Initial IoC types:

- IPv4 addresses
- IPv6 addresses
- Domains
- URLs
- File hashes

Future:

- SSL/TLS certificates
- Other STIX objects

---

## 5. Core Features

### MVP

- IoC lookup
- Threat feed ingestion
- Data normalization
- IoC deduplication
- Source correlation
- IoC storage
- Basic risk assessment
- Web dashboard
- REST API

### Future Features

- Continuous feed monitoring
- Automated alerts
- Reputation change detection
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

The initial version will focus on collecting and correlating
threat intelligence data from multiple external sources.

The platform will not independently discover malicious activity.
Instead, it will aggregate, normalize, correlate, and monitor
information provided by external threat intelligence sources.

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
