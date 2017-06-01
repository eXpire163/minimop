from minimop.helper.mathf import Mathf


def capital_case(mixcase):
    return mixcase.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_mathf_clamp():
    assert Mathf.clamp(10, 0, 1) == 1
    assert Mathf.clamp(0.53, 0, 1) == 0.53

def test_mathf_smooth():
    assert Mathf.smoothstep(0, 1, 0.5) == 0.5
    assert Mathf.smoothstep(0, 1, 0.2) == 0.104

def test_mathf_sclae():
    assert round(Mathf.scale(15, 10.0, 20.0, 0.0, 1.0), 2) == 0.5
