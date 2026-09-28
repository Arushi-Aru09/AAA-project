# AAA Metrics

## Verdict Classification

### Consistent
Outcome differs: No

Expected to change: No

Meaning:
The outcome remained the same and no change was expected.

---

### Unexpected Divergence
Outcome differs: Yes

Expected to change: No

Meaning:
The outcome changed even though no meaningful change was expected. This is the most important finding because it indicates inconsistent behavior.

---

### Expected Divergence
Outcome differs: Yes

Expected to change: Yes

Meaning:
The outcome changed because a meaningful input change was introduced. This is expected behavior.

---

### Missed Sensitivity
Outcome differs: No

Expected to change: Yes

Meaning:
A meaningful change was introduced, but the outcome did not change. This may indicate that the system is not sensitive to important inputs.

---

## final_decision

Comparison method: Exact string equality.

Case-sensitive: Yes.

Any difference counts as an outcome difference.

Examples:

Approve = Approve

Approve != approve

Approve != APPROVE

---

## final_settlement_gbp

Settlement values differ if:

abs(a - b) / max(abs(a), abs(b)) > 0.05

Default tolerance: 0.05 (5%).

Examples:

1000 vs 1040 = No difference

1000 vs 1200 = Difference

---

## agents_visited

Recorded as: routing_differs

This is a secondary signal only.

Different routes can legitimately reach the same correct outcome. Therefore route differences alone should not be treated as an outcome difference.

Reason:

Counting every routing difference as an outcome difference would create many false positives. The final outcome is more important than the path taken to reach it.
## Settlement Edge Cases

### Both None
Not Different

### One None and One Numeric
Different

### Both 0.0
Not Different

### Exactly At Tolerance
Not Different

## Structural Edge Cases

### Missing Partner Run
Flag as incomplete pair.

### One Run Failed
Comparison not possible.

### Both Runs Failed
Report pair failure.

### More Than Two Runs
Flag additional runs.

## Shared Base Run

Flag affected pairs.

Reason:
If a base run is unreliable, every pair using that base run may also be unreliable.

## Tolerance Rule

Tolerances must be fixed before measurement and should never be changed later to improve results.

## Aggregate Metrics

### unexpected_divergence_rate

unexpected_divergence / pairs where no change was expected

### missed_sensitivity_rate

missed_sensitivity / pairs where change was expected

## Report Metadata

- dataset_path
- seed
- commit_hash
- tolerance
- generated_at