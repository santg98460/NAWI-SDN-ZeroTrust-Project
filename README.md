# NAWI Network Integration – SDN, Zero Trust & Multi-Site Failover Design

**Course**: INFO6033-01 – Network & Security Architecture  
**Institution**: Fanshawe College (Postgraduate Program)  
**Role**: Project Manager & Lead Designer (Student – Santosh Giri)  
**Date**: Winter 2026

---

## 📌 Project Overview

Designed a complete network integration for **North American Widget Inc. (NAWI)** , a fictitious company formed by merging Canadian (GCWC) and US (GAWC) operations. The solution unifies both networks using **SDN (OpenDaylight)** , **Zero Trust security**, **private/public cloud**, and **active failover** across three data centres (Toronto, Dallas, Markham).

---

## 🎯 Problem Statement

- GCWC (Canada) had modern SD-WAN but traditional core networking.
- GAWC (USA) ran on legacy Frame Relay with no cloud or backup data centre.
- Required: Unified, secure, compliant, and highly available network across both countries.

---

## 🔧 Technologies & Concepts Used

| Category | Technologies |
|----------|--------------|
| **SDN Controller** | OpenDaylight (3-node clusters in Toronto, Dallas, Markham + cloud DR) |
| **Switching Fabric** | White-box switches (Edge-Core AS7712, AS4610) + Open vSwitch + Cumulus Linux |
| **SD-WAN** | 10GbE IPsec tunnel between Toronto–Dallas, BGP routing |
| **Zero Trust** | MFA (Azure AD), micro-segmentation, device compliance (Intune), ZTNA (replaces VPN), continuous monitoring (Azure Sentinel) |
| **Cloud** | Private clouds (Toronto & Dallas for data residency) + Public cloud (Dallas for shared services) |
| **Data Isolation** | VRF, BGP communities, ACLs, SDN flow rules (PIPEDA, CCPA, TDPSA compliance) |
| **Failover/DR** | Active failover via Markham; RTO 30 seconds, RPO 0 minutes for critical systems |
| **Management** | Centralized "single pane of glass" + isolated management cloud (VLAN 70) |

---

## 🏗️ High-Level Architecture
Canadian Region (Northern Failure Domain)
├── Toronto DC (Primary) – SDN + Private Cloud + Management Cloud
├── Markham DC (Backup for both Canada & US) – Active failover
├── 4 Regional Offices + 14 Branches
└── 100GbE replication Toronto ↔ Markham

US Region (Southern Failure Domain)
├── Dallas DC (Primary) – SDN + Private Cloud + Public Cloud + Management Cloud
├── 3 Regional Offices + Independent Sales Agents
├── 100GbE replication Dallas ↔ Markham

Cross-Border
├── 40GbE SD-WAN Toronto ↔ Dallas (BGP, IPsec)
└── Backup path via Markham if direct link fails

---

## 📊 Key Metrics Achieved

| Metric | Target | Achieved |
|--------|--------|----------|
| Provisioning time | Days → Minutes | ✅ |
| RTO (critical systems) | 30 seconds | ✅ |
| RPO (critical databases) | 0 minutes | ✅ |
| Data residency compliance | PIPEDA, CCPA, TDPSA | ✅ |
| Zero cross-border data leak | Yes | ✅ |
| Unified management | Single pane of glass | ✅ |

---

## 📁 Project Artifacts in This Repository

| File | Description |
|------|-------------|
| `NAWI_Project_Report_Group5.pdf` | Full 14‑section project report (executive summary, design, zero trust, failover, benefits, risks, references) |
| `diagrams/` | Network topology, SDN controller distribution, failover flows |
| `configs/` | Sample BGP, OpenFlow, and VLAN configurations |

> **Note**: Full report available in PDF. Configuration snippets and diagrams are included for quick review.

---

## 🧠 What I Learned / Demonstrated

- How to design a **multi-site SDN fabric** using open standards (OpenDaylight, OpenFlow 1.3)
- How to implement **Zero Trust** (MFA, micro-segmentation, ZTNA, continuous monitoring)
- How to enforce **data residency** (VRF, BGP, SDN flow rules) for PIPEDA/CCPA/TDPSA
- How to build **active-active failover** with 30‑second RTO across three data centres
- How to integrate **private + public cloud** while maintaining isolation
- How to **manage the entire network from a single pane of glass**

---

## 📫 Contact

**Santosh Giri**  
📧 giri.santosh1980@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/santosh-giri-991326b7/)  
💻 [GitHub](https://github.com/Santosh-Giri) (you)

---

*This project was completed as part of the Postgraduate Network & Security Architecture program at Fanshawe College.*
