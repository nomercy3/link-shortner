from src.redis_service.service import RedisService

from pytest import fixture, raises


@fixture
def redis_service() -> RedisService:
    return RedisService()


def test_save_data_type(redis_service):
    with raises(TypeError):
        assert redis_service.save_data(data=123)
