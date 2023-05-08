from src.shortner.service import ShortnerService

from pytest import fixture, raises


@fixture
def shortner_service() -> ShortnerService:
    return ShortnerService()


def test_make_short(shortner_service, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'test_url')
    assert isinstance(shortner_service.make_short(), str)


def test_get_full_link(shortner_service, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'test_url')
    assert isinstance(shortner_service.get_full_link(), str)


