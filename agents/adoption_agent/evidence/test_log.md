# Assignment 6 actual run log

Student: Shuoying Wang. All times are America/New_York dates. Prompts were built with the supplied scaffold; JSON responses were authored in this ChatGPT/Codex session using the prompt content and the original sources in `source_register.md`. They are model-assisted case analyses, not live Waymo operations or an API benchmark. The local checker tests contract shape, not whether the decision is sound.

## 2026-10-24 initial primary run, v0.1

1. Ran `python3 tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json`. It produced `work/adoption_agent_primary_prompt.txt` (ignored generated packet).
2. Evaluated that packet in ChatGPT/Codex and saved `responses/primary_v0_1_weak.json`.
3. Ran `python3 tools/validate_response.py agents/adoption_agent/responses/primary_v0_1_weak.json`: **VALIDATION PASSED**.
4. Ran `python3 tools/check_frozen_core.py`: **FROZEN CORE INTACT**.
5. Substantive review: **FAILED**. The response recommends 100 passenger rides now despite admitting there is no verified contract, integration access, permit responsibility, insurance arrangement, or current recall remedy status. A schema-valid response is not permission to operate. The v0.1 instruction merely said to mention missing evidence, so it failed to make missing safety/commercial gates constrain its action.

## Revision target

Replace the vague “prefer a limited pilot” rule with named action categories, decision gates, a no-passenger preflight phase, explicit counterevidence handling, and a route to request more evidence. Then run primary, risk-posture contrast, and insufficient-evidence cases through the actual prompt builder and validator.
