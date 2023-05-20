from src.shortner.service import ShortnerService

from fastapi import APIRouter, Response

shortner_router = APIRouter()
shortner_service = ShortnerService()


@shortner_router.get(
    '/get-short-link',
    summary='Get Short Link',
    description='Shortens Passed Link'
)
def shorten_link(link: str):
    try:
        data = shortner_service.shorten(link)
        return data

    except TypeError:
        return Response(status_code=300, content='Bad Request')
    except ConnectionError:
        return Response(status_code=500, content='Internal Server Error')


@shortner_router.get(
    '/get-full-link',
    summary='Get Full Link',
    description='Returns Full Link by Passed Link'
)
def get_full_link(link: str):
    try:
        data = shortner_service.full_link(link)
        print(data)
        return data
    except TypeError:
        return Response(status_code=300, content='Bad Request')
    except ValueError:
        return Response(status_code=404, content='Not Found')
    except ConnectionError:
        return Response(status_code=500, content='Internal Server Error')
