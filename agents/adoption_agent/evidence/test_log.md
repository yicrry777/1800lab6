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

## 2026-10-24 revised run, v1.0

1. Rebuilt three actual prompt packets using `tools/build_prompt.py`: `primary.json`, `contrast_1.json`, and `contrast_2.json`. Each command returned a generated path under ignored `work/`.
2. Evaluated each case in this ChatGPT/Codex session using the revised specialist instructions and the checked original sources; saved the three `responses/*_response.json` files. This is not a live operation, independent model benchmark or OpenAI API call.
3. Ran `tools/validate_response.py` separately on all three final JSON responses: **VALIDATION PASSED** for each.
4. Ran `agents/adoption_agent/verify_cases.py`: **SEMANTIC CASE CHECK PASSED**. The general Waymo finding is exactly identical in the three outputs. Present recommendations are **PROOF OF CONCEPT**, **DEFER**, and **REQUEST MORE EVIDENCE** respectively, and all prohibit current passenger rollout.
5. Ran `tools/check_frozen_core.py`: **FROZEN CORE INTACT**. Ran `git diff --exit-code main -- core tools`: no differences. Ran `python3 -m compileall -q agents/adoption_agent/verify_cases.py`: exit 0.

## What stayed stable and what changed

The general finding stayed stable: Waymo has commercial Phoenix operations and substantial rider-only deployment, while the Waymo evidence is operational-domain limited and the 2026 construction-zone recall is material. The application and organization judgment changed: a moderate private ride-hail platform can do non-passenger diligence, whereas a conservative public provider with unproven accessible equivalent service should defer a public passenger offering. When route/coverage and vendor access are omitted, the response explicitly requests more evidence instead of choosing a pilot by default.

## Remaining limitations

The fictional organizations supplied no internal records. No Waymo partner agreement, dispatch API rights, route-level demand, current fleet remedy status, accessible-service audit, permit/insurance allocation, or unit economics were verified. The local validator checks structure, and `verify_cases.py` checks a few decision invariants; neither verifies every substantive claim or certifies a live service. Recheck changing vendor and regulatory sources before any real decision.
