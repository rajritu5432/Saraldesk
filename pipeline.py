"""On-device pipeline skeleton: OCR -> Privacy Shield -> local LLM -> (TTS).

Status: scaffold. Model loading is stubbed so the structure and Privacy Shield can be
tested anywhere. On a Snapdragon X-series PC, replace the stubs with Qualcomm AI Hub
models running through ONNX Runtime (QNN execution provider) and the Genie / GenieX
LLM service. See docs/ARCHITECTURE.md.
"""
from dataclasses import dataclass
from .privacy_shield import mask_pii


def available_providers():
    """List ONNX Runtime execution providers; QNN indicates NPU access on Snapdragon."""
    try:
        import onnxruntime as ort
        return ort.get_available_providers()
    except ImportError:
        return ["onnxruntime not installed"]


@dataclass
class Explanation:
    masked_text: str
    pii_found: list
    summary: str


def run_ocr(image_path: str) -> str:
    raise NotImplementedError("Load PP-OCR (QNN/NPU) here and return the recognised text.")


def explain(document_text: str) -> Explanation:
    masked, found = mask_pii(document_text)
    # TODO: send masked text to the local LLM (Genie / GenieX, NPU) with a prompt that answers
    # only from the document and lists key dates, amounts and a to-do checklist.
    return Explanation(masked, found, "[LLM summary placeholder: connect the local model here]")
