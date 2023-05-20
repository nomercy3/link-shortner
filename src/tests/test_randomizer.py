from pytest import fixture

from src.randomizer.service import RandomizerService


class TestRandomizerService:
    @fixture
    def randomizer_service(self) -> RandomizerService:
        return RandomizerService()

    @fixture
    def test_link(self) -> str:
        return 'https://mytest.domain/folder/folder/123123?type=314'

    def test_make_random_path_len(self, randomizer_service):
        random_path = randomizer_service.make_random_path()
        assert len(random_path) == 10

    def test_make_random_path(self, randomizer_service, test_link):
        random_path = randomizer_service.make_random_path()
        assert random_path != test_link

    def test_make_random_path_random(self, randomizer_service):
        first_random_path = randomizer_service.make_random_path()
        second_random_path = randomizer_service.make_random_path()

        assert first_random_path != second_random_path
