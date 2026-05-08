# Paper 1 Planning Note

## Working Title

**CyberXTalk: A Context-Aware Multilingual Cyber Incident Reporting and Intelligence Framework for Pre-CERT Triage in Low-Resource Digital Economies**

## Central Thesis

CyberXTalk is a pre-CERT cyber incident intelligence framework designed to transform informal, multilingual, human-generated cybercrime narratives into structured, actionable intelligence for classification, triage, evidence capture, escalation, and response support.

## Strategic Positioning

CyberXTalk does not compete with CERTs, SIEMs, SOAR platforms, police cybercrime portals, banking fraud desks, or institutional incident response teams.

Instead, it operates before formal response systems by helping non-technical users submit usable incident reports and helping response actors receive structured intelligence rather than raw complaints.

## Problem Statement

In low-resource digital economies, many cyber incidents are reported informally through phone calls, WhatsApp messages, social media complaints, physical reports, banking complaints, and scattered institutional channels. These reports are often incomplete, multilingual, emotionally expressed, and technically unstructured.

Formal response institutions require structured incident intelligence, but ordinary victims rarely describe cyber incidents using standard cyber-response terminology. This creates a gap between victim reporting and institutional response readiness.

## Research Gap

Existing cybersecurity reporting and response systems tend to assume one or more of the following:

1. The reporter has technical literacy.
2. The report is submitted through a formal portal.
3. The data is already structured.
4. The incident is represented through logs or machine telemetry.
5. The language of reporting is formal English or a standardized cybersecurity vocabulary.

CyberXTalk addresses a different problem: informal human cybercrime reports in multilingual, low-resource environments.

## Core Research Questions

1. How can informal human-generated cybercrime narratives be transformed into structured cyber incident intelligence?
2. What components are required for a pre-CERT cyber incident reporting and intelligence framework?
3. How can multilingual and context-aware reporting improve incident triage and escalation in low-resource digital economies?
4. How can CyberXTalk complement existing response institutions without claiming to replace them?

## Objectives

1. To design a context-aware pre-CERT cyber incident reporting framework.
2. To define the core architectural components of CyberXTalk.
3. To model how informal reports can be converted into structured cyber incident objects.
4. To propose a triage and escalation workflow for cyber incident response support.
5. To establish the foundation for later work on taxonomy, classification, and multilingual NLP.

## Expected Contributions

1. A pre-CERT conceptual positioning for citizen/SME-facing cyber incident intelligence.
2. A framework architecture for multilingual incident intake, structuring, triage, evidence capture, and escalation.
3. A human-report-centered incident intelligence pipeline distinct from log analytics.
4. A low-resource digital economy framing for cyber incident reporting.
5. A publication foundation for subsequent CyberXTalk papers.

## Proposed Methodology

This paper can be structured as a design science research paper.

### Phase 1: Problem Identification

Identify the reporting gap between informal victim narratives and formal response requirements.

### Phase 2: Framework Design

Design CyberXTalk as a modular framework with the following components:

- User incident intake interface
- Multilingual narrative capture
- Guided reporting assistant
- Evidence upload/capture module
- Incident normalization layer
- Structured incident object generator
- Classification and triage engine
- Escalation recommendation layer
- Response-support dashboard
- Analytics and intelligence reporting layer

### Phase 3: Scenario-Based Demonstration

Use realistic cyber incident reporting scenarios to show how the framework processes raw reports.

Example scenarios:

- Phishing link leading to bank credential theft
- WhatsApp account takeover
- Unauthorized bank debit alert
- Social media impersonation scam
- SME business email compromise complaint

### Phase 4: Evaluation Strategy

Evaluate the framework using criteria such as:

- Completeness of captured incident information
- Clarity of structured incident output
- Suitability for triage
- Escalation usefulness
- Usability for non-technical reporters
- Adaptability to multilingual reporting contexts

## Proposed Paper Structure

### Abstract

Briefly state the reporting gap, CyberXTalk approach, framework components, and expected contribution.

### 1. Introduction

Discuss rising cybercrime, underreporting, informal reporting channels, fragmented response pathways, and the need for a pre-CERT intelligence layer.

### 2. Background and Related Work

Cover CERTs, cyber incident reporting systems, SIEM/SOAR distinction, threat intelligence, low-resource cybersecurity, cybercrime reporting, and multilingual NLP challenges.

### 3. Problem Context and Motivation

Explain why ordinary cybercrime reports are not logs, why formal systems struggle with informal narratives, and why low-resource environments require a special framework.

### 4. CyberXTalk Framework Design

Present the architecture, modules, data flow, actor roles, and output intelligence objects.

### 5. Pre-CERT Triage and Escalation Workflow

Show how reports move from raw complaint to structured incident record, severity level, and recommended escalation pathway.

### 6. Demonstration Scenarios

Use sample incident narratives to demonstrate how the framework works.

### 7. Evaluation Plan

Define how the framework can be evaluated using expert review, scenario walkthroughs, usability assessment, and structured-output quality.

### 8. Discussion

Discuss practical implications, limitations, institutional integration, ethical concerns, privacy, and responsible disclosure boundaries.

### 9. Conclusion and Future Work

Summarize the framework and link future papers: taxonomy/schema, classification/triage, and multilingual NLP.

## Things to Avoid

- Do not claim CyberXTalk replaces CERTs.
- Do not overclaim national cybersecurity control.
- Do not lead with generic "machine learning" language.
- Do not confuse human incident reports with machine logs.
- Do not expose real victim data or sensitive operational claims.

## Strong One-Sentence Framing

CyberXTalk is a pre-CERT cyber incident intelligence framework that converts messy, multilingual human cybercrime reports into structured, actionable intelligence for triage, escalation, and response support.
