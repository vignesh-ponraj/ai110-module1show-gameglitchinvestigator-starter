import ast
from pathlib import Path

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# Tested: attempt limits are ordered Easy > Normal > Hard
def test_attempt_limits_are_ordered_easy_normal_hard():
    """Regression test for difficulty attempt limit ordering bug."""
    app_path = Path(__file__).resolve().parents[1] / "app.py"
    app_source = app_path.read_text(encoding="utf-8")
    module = ast.parse(app_source)

    attempt_limit_map = None
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "attempt_limit_map":
                    attempt_limit_map = ast.literal_eval(node.value)
                    break
        if attempt_limit_map is not None:
            break

    assert attempt_limit_map is not None
    assert attempt_limit_map["Easy"] > attempt_limit_map["Normal"]
    assert attempt_limit_map["Normal"] > attempt_limit_map["Hard"]
