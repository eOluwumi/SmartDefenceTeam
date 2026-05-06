"""
CyberXTalk YarnGPT TTS Proof-of-Concept

This script tests YarnGPT as the Nigerian-accented voice-output layer for
CyberXTalk. It assumes it is executed from a runtime where the YarnGPT
repository or package is available.

Important:
- Do not commit model checkpoints, generated audio, or Hugging Face caches.
- The WavTokenizer checkpoint and config must be downloaded locally before use.
- In Codespaces, soundfile is used instead of torchaudio.save to avoid
  TorchCodec / FFmpeg compatibility issues.
"""

from pathlib import Path

import soundfile as sf
import torch
from transformers import AutoModelForCausalLM

from audiotokenizer import AudioTokenizerV2


TOKENIZER_PATH = "saheedniyi/YarnGPT2"
WAV_TOKENIZER_CONFIG_PATH = "wavtokenizer_mediumdata_frame75_3s_nq1_code4096_dim512_kmeans200_attn.yaml"
WAV_TOKENIZER_MODEL_PATH = "wavtokenizer_large_speech_320_24k.ckpt"
OUTPUT_FILE = "cyberxtalk_yarngpt_sample.wav"
SAMPLE_RATE = 24000


def assert_runtime_assets_exist() -> None:
    """Fail early if the required local WavTokenizer files are missing."""
    required_files = [
        WAV_TOKENIZER_CONFIG_PATH,
        WAV_TOKENIZER_MODEL_PATH,
    ]

    missing = [path for path in required_files if not Path(path).exists()]

    if missing:
        missing_list = "\n".join(f"- {path}" for path in missing)
        raise FileNotFoundError(
            "Missing required local runtime assets:\n"
            f"{missing_list}\n\n"
            "Download them locally before running this test. "
            "Do not commit these files to the repository."
        )


def main() -> None:
    assert_runtime_assets_exist()

    text = (
        "This appears to be a high risk phishing incident. "
        "Please contact your bank immediately, block the affected account, "
        "change your password, and preserve the suspicious message as evidence."
    )

    print("Loading audio tokenizer...")
    audio_tokenizer = AudioTokenizerV2(
        TOKENIZER_PATH,
        WAV_TOKENIZER_MODEL_PATH,
        WAV_TOKENIZER_CONFIG_PATH,
    )

    print(f"Using device: {audio_tokenizer.device}")

    print("Loading YarnGPT model...")
    model = AutoModelForCausalLM.from_pretrained(
        TOKENIZER_PATH,
        torch_dtype=torch.float32,
    ).to(audio_tokenizer.device)
    model.eval()

    print("Creating prompt...")
    prompt = audio_tokenizer.create_prompt(
        text,
        lang="english",
        speaker_name="idera",
    )

    input_ids = audio_tokenizer.tokenize_prompt(prompt)
    attention_mask = torch.ones_like(input_ids)

    print("Generating audio tokens...")
    with torch.no_grad():
        output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            do_sample=False,
            repetition_penalty=1.1,
            max_new_tokens=300,
            pad_token_id=model.config.eos_token_id,
        )

    print("Extracting codes...")
    codes = audio_tokenizer.get_codes(output)
    print(f"Number of audio codes: {len(codes)}")

    if not codes:
        raise RuntimeError("No audio codes generated. Try increasing max_new_tokens.")

    print("Decoding audio...")
    audio = audio_tokenizer.get_audio(codes)

    audio_np = audio.squeeze().detach().cpu().numpy()
    sf.write(OUTPUT_FILE, audio_np, SAMPLE_RATE)

    print(f"Saved {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
