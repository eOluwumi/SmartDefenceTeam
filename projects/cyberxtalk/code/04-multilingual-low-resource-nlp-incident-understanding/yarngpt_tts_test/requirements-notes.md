# Requirements Notes

The original YarnGPT test was run from the upstream YarnGPT repository in GitHub Codespaces.

## Core Packages Used

```text
outetts
uroman
torch
torchaudio
transformers
inflect
soundfile
```

## Runtime Assets

The test required:

```text
wavtokenizer_large_speech_320_24k.ckpt
wavtokenizer_mediumdata_frame75_3s_nq1_code4096_dim512_kmeans200_attn.yaml
saheedniyi/YarnGPT2
```

These files should not be committed to this repository.

## Saving Audio

`torchaudio.save()` failed in Codespaces because of TorchCodec / FFmpeg compatibility issues.

The fix was to use `soundfile`:

```python
audio_np = audio.squeeze().detach().cpu().numpy()
sf.write(output_file, audio_np, 24000)
```
