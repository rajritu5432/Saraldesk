# Architecture

Input (camera/scanner/PDF, mic) -> Perception on NPU (OCR, speech recognition) -> Privacy Shield (CPU) -> Reasoning on NPU (quantised small LLM) -> Output (screen, TTS, encrypted local store, local reminders).

| Task | Model approach | Runtime |
|---|---|---|
| Speech recognition | Whisper family from Qualcomm AI Hub | ONNX Runtime + QNN, NPU |
| OCR | PP-OCR-class; Indic recogniser planned | QNN, NPU |
| Q&A | Quantised open-weight small LLM via Genie / GenieX | NPU |
| TTS | MeloTTS-class (English); Indic TTS planned | NPU / CPU |
| PII | Regex + checksum (this repo) | CPU |
