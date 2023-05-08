from src.shortner.service import ShortnerService


def main():
    service = ShortnerService()
    service.make_short()
    service.get_full_link()


if __name__ == '__main__':
    main()
