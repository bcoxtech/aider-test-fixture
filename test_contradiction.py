# Deliberately contradictory test fixture for agent-dispatcher pilot
# validation (CLA-289): both assertions call subtract(10, 3) and demand two
# different results, so no pure implementation of subtract can ever satisfy
# both. Used to force a guaranteed-failing retry/circuit-breaker cycle
# (dispatcher's agent-cycle-1 -> agent-cycle-2 -> agent:failure path)
# regardless of how capable the coding model is. Not a real bug report.
from contradiction import subtract


def test_subtract_contradiction():
    assert subtract(10, 3) == 6
    assert subtract(10, 3) == 8
