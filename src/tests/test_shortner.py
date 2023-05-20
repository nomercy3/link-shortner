from src.shortner.service import ShortnerService
from src.redis_service.service import RedisService

from pytest import fixture, raises
from unittest import mock
from dotenv import load_dotenv
from os import getenv


class TestShortnerService:
    @fixture
    def shortner_service(self) -> ShortnerService:
        yield ShortnerService()

    @fixture
    def mocked_redis_service(self) -> RedisService:
        with mock.patch(
                'src.shortner.service.ShortnerService.redis_service',
                autospec=True
        ) as MockRedisService:
            yield MockRedisService

    @fixture
    def load_env(self) -> {}:
        load_dotenv()
        return {
            'DOMAIN': getenv('DOMAIN')
        }

    def test_shorten_connection(self, shortner_service, mocked_redis_service):
        mocked_redis_service.save_data.side_effect = ConnectionError
        with raises(ConnectionError):
            shortner_service.shorten(full_link='https://jhasdhjasd')

    def test_shorten_type(self, shortner_service):
        with raises(TypeError):
            shortner_service.shorten(full_link=123)

    def test_shorten_return(self, shortner_service, mocked_redis_service, load_env):
        result = shortner_service.shorten(full_link='https://test_link.com')

        assert load_env.get('DOMAIN') in result
        assert len(result[::-1][:10]) >= 10
