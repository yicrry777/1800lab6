"""Small semantic regression check for the submitted three-case comparison.

Run after the frozen scaffold's JSON contract validator. This does not judge safety
or replace source review; it catches the context-insensitivity found during testing.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
responses = {name: json.loads((root / 'responses' / f'{name}_response.json').read_text())
             for name in ('primary', 'contrast_1', 'contrast_2')}
expected = {'primary': 'PROOF OF CONCEPT', 'contrast_1': 'DEFER',
            'contrast_2': 'REQUEST MORE EVIDENCE'}
assert len({r['general_et_finding'] for r in responses.values()}) == 1, 'General Waymo finding drifted with context'
for name, response in responses.items():
    rec = response['recommendation_management_implication']
    assert rec.startswith(expected[name] + ' —'), f'{name}: wrong current posture'
    assert all(item['source_or_reference'].startswith('https://') and item['date_or_recency']
               for item in response['evidence']), f'{name}: undated or nonlinked evidence'
    assert response['abstention_or_more_information_needed'], f'{name}: missing evidence/abstention note'
assert 'No live passenger trips' in responses['primary']['risk_governance_implication']
assert 'Withhold public passenger rollout' in responses['contrast_1']['risk_governance_implication']
assert 'Do not commit to integration or passenger testing' in responses['contrast_2']['risk_governance_implication']
print('SEMANTIC CASE CHECK PASSED: stable general finding, three distinct postures, dated evidence, and no live launch')
