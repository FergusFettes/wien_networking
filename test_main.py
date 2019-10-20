import pytest


from main import Bezirk

def test_bezirk_initialized_okay():
    with pytest.raises(NameError):
        Bezirk()
    Bezirk(1)
    Bezirk(23)
    with pytest.raises(NameError):
        Bezirk(24)
    Bezirk("1010")
    Bezirk("1230")
    with pytest.raises(NameError):
        Bezirk("1240")

def test_values_initialized_from_name():
    m = Bezirk(name="Mariahilf")
    assert type(m.name) is str
    assert m.name is not ''
    assert type(m.number) is int
    assert type(m.postleitzahl) is str
    assert m.postleitzahl is not ''

def test_values_initialized_from_number():
    m = Bezirk(number=6)
    assert type(m.name) is str
    assert m.name is not ''
    assert type(m.number) is int
    assert type(m.postleitzahl) is str
    assert m.postleitzahl is not ''

def test_values_initialized_from_postleitzahl():
    m = Bezirk(postleitzahl="1060")
    assert type(m.name) is str
    assert m.name is not ''
    assert type(m.number) is int
    assert type(m.postleitzahl) is str
    assert m.postleitzahl is not ''


