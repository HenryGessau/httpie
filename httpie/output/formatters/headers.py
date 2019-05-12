from httpie.plugins import FormatterPlugin


QUASHED = [

    # Request
    'Accept',
    'Accept-Encoding',
    'Authorization',
    'Connection',
    'Host',
    'User-Agent',

    # Response
    'Connection',
    'Cache-Control',
    'Content-Encoding',
    'Content-Security-Policy',
    'Content-Type',
    # 'Date',
    'Expect-CT',
    'Expires',
    'Pragma',
    'Referrer-Policy',
    'Server',
    'Set-Cookie',
    'Strict-Transport-Security',
    'Transaction-Id',
    'Transfer-Encoding',
    'X-Content-Type-Options',
    'X-Frame-Options',
    'X-XSS-Protection',
]


class HeadersFormatter(FormatterPlugin):

    def format_headers(self, headers: str) -> str:
        """
        Sorts headers by name while retaining relative
        order of multiple headers with the same name.

        """
        lines = headers.splitlines()
        headers = sorted(lines[1:], key=lambda h: h.split(':')[0])
        headers = [h for h in headers if h.split(':')[0] not in QUASHED]
        return '\r\n'.join(lines[:1] + headers)
