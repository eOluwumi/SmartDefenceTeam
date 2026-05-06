# YarnGPT TTS Test for CyberXTalk

This folder contains the CyberXTalk voice-response proof-of-concept using YarnGPT.

## Purpose

The goal is to test whether YarnGPT can serve as the Nigerian-accented text-to-speech output layer for CyberXTalk.

## Proven Milestone

A test run inside GitHub Codespaces successfully generated a CyberXTalk-style voice response and saved it as a `.wav` file.

```text
Saved cyberxtalk_yarngpt_sample.wav
```

## Position in CyberXTalk

YarnGPT should be treated as a voice-output layer, not the entire CyberXTalk intelligence engine.

```text
User Voice Input
   ↓
STT Layer: Whisper / Azure Speech / YarnGPT ASR experiment
   ↓
CyberXTalk Incident Intelligence Engine
   ↓
Generated Response Text
   ↓
YarnGPT TTS
   ↓
Nigerian-accented Spoken Response
```

## Local Runtime Notes

This test requires external model assets and should not commit runtime files.

Do not commit:

- `.ckpt`
- `.safetensors`
- `.wav`
- `.mp3`
- downloaded model caches
- secrets or API keys

## Expected Files

```text
yarngpt_tts_test/
├── README.md
├── test_cyberxtalk_yarngpt_tts.py
└── requirements-notes.md
```

## Next Step

Convert this proof-of-concept into a clean service boundary that CyberXTalk can call when it needs to generate spoken responses.
