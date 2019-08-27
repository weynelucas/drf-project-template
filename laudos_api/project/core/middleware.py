from .loader import get_revison


class RevisionMiddleware:
    """
    Middleware component which will modify every response to include the header
    with the source revision (last commit id) information
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        source_revision = get_revison()

        if source_revision:
            response['X-Source-Revision'] = source_revision

        return response
