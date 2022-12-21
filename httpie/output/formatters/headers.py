from ...plugins import FormatterPlugin


QUASHED = [

    # Request
    'accept',
    'accept-encoding',
    'authorization',
    'connection',
    'content-length',
    'host',
    'user-agent',

    # Response
    'allow-snippet-annotations',
    'cf-cache-status',
    'cache-control',
    'connection',
    'content-encoding',
    'content-security-policy',
    'content-type',
    'expect-ct',
    'expires',
    'pragma',
    'referrer-policy',
    'server',
    'set-cookie',
    'strict-transport-security',
    'transaction-id',
    'transfer-encoding',
    'vary',
    'x-content-type-options',
    'x-frame-options',
    'x-xss-protection',
]


class HeadersFormatter(FormatterPlugin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enabled = self.format_options['headers']['sort']

    def format_headers(self, headers: str) -> str:
        """
        Sorts headers by name while retaining relative
        order of multiple headers with the same name.

        """
        lines = headers.splitlines()
        headers = sorted(lines[1:], key=lambda h: h.split(':')[0])
        headers = [h for h in headers if h.lower().split(':')[0] not in QUASHED]
        return '\r\n'.join(lines[:1] + headers)
