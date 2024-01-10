from python_ci_code_coverage.hello import call_hello

def test_hello():
    assert call_hello() == "hey, its me!"