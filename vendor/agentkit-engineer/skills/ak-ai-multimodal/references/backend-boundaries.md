# Multix versus host-native multimodal capability

The AgentKit 2.19.0 upstream SKILL.md pins `@mrgoonie/multix@0.2.0` and describes audio, video, music, image and document operations over changing Google/OpenRouter/MiniMax catalogs. This file is a **workflow crosswalk**, not an installed CLI.

| Operation | Minimum valid substitute | Evidence required |
|---|---|---|
| Visual/OCR question | Structured extraction or real image vision | Identified source, visible region/page, uncertain characters |
| Image generation/edit | Image-generation API or editor | Actual image result, constraint check, editable requirement when named |
| Audio transcription | Recognized audio/transcript tool | Time-aligned source, language, uncertain words |
| Speech/music synthesis | Supported generation provider | License/consent, actual playable audio, model/backend |
| Video understanding | Decoder or capable multimodal provider | Frame/timestamps, omissions and sampling limitations |
| Video generation | Capable video backend | Actual file/frames/duration, privacy/cost |
| PDF/document | Structured parser first; visual check for layout | Page/section provenance, layout and extraction limits |

For native usage, use the **installed** `multix ... --help` for each operation rather than copying version-sensitive flags. An unavailable modality remains unavailable; claiming 'multimodal support' generically does not mean every row is executable. Optional image/video provider quotas and model prices change; verify at execution. External media uploads are separate privacy/authority decisions.
