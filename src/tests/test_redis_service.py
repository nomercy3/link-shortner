from src.redis_service.service import RedisService

from pytest import fixture, raises

@fixture
def redis_service() -> RedisService:
    service = RedisService()
    return service


def test_get_value_for_key_raises_type_error(redis_service):
    with raises(TypeError):
        redis_service.get_value_for_key(
            key=123
        )

def test_set_key_value_raises_type_error(redis_service):
    with raises(TypeError):
        redis_service.set_key_value(
            key=123,
            value=321
        )

def test_set_key_value(redis_service):
    redis_service.set_key_value(
        key='test_key',
        value='test_value'
    )

