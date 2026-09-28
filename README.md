# SaralDesk

Private, offline, voice-first document copilot for Snapdragon-powered HP PCs, built for the Snapdragon AI Lab Build & Present Challenge.

Scan a form, notice or bill. SaralDesk reads it on-device, explains it in plain Hindi, Bengali or English, lists what to do and by when, and answers spoken follow-up questions. Sensitive identifiers are masked locally and no document leaves the PC.

## Status
Early prototype scaffold. Implemented and tested: the **Privacy Shield** (Aadhaar with Verhoeff checksum, PAN, phone, account numbers). The pipeline structure is in place; model loading (OCR, Whisper, local LLM, TTS) is stubbed and is the next step on a Snapdragon X-series PC.

## Planned models
Whisper (Qualcomm AI Hub), PP-OCR-class OCR, quantised small LLM via Genie / GenieX, MeloTTS-class TTS. Indic-script OCR and Indic TTS are planned and need conversion.

## Run the tests
    pip install -r requirements.txt
    PYTHONPATH=src pytest

## Targets to validate on device
One-page document summarised in under 20 s; speech real-time factor below 0.5; NPU-vs-CPU latency, CPU load and battery reported.

## Docs
See docs/ARCHITECTURE.md.

## License
MIT
