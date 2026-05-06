# Paper 3: Context-Aware Cyber Incident Classification and Triage

## Working Title

**Context-Aware Cyber Incident Classification and Triage from Informal User Reports Using Transformer-Based Language Models**

## Core Idea

This paper focuses on the intelligence pipeline that classifies informal cybercrime reports into actionable categories and assigns triage priority.

## Research Gap

Many cyber incident classification systems assume structured inputs, technical logs, or well-formed reports. CyberXTalk assumes the opposite: noisy, incomplete, informal, user-generated narratives.

## Contribution

- Classification pipeline for informal cyber incident narratives.
- Triage logic combining incident type, severity, evidence, affected institution, and reported loss.
- Transformer-based modelling strategy as one part of a broader engineered workflow.
- Structured output for escalation and response support.

## Possible Target Classes

- Phishing
- Online banking fraud
- Social media account compromise
- Identity impersonation
- Malware infection
- Ransomware/extortion
- Romance/investment scam
- Unauthorized transaction
- Data breach/privacy violation
- Business email compromise
- Unknown/other

## Possible Research Questions

1. How accurately can informal user-generated cybercrime narratives be classified into incident categories?
2. How can context-aware features improve triage beyond ordinary text classification?
3. How can a classification pipeline produce actionable outputs for pre-CERT escalation?

## Notes

Do not position this paper as merely "using machine learning." The real contribution is the classification-to-triage pipeline for messy human reports.
