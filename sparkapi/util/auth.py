import hmac
import base64
import hashlib
import textwrap

from urllib.parse import urlencode, urlparse

from .common import generate_rfc1123_date


def get_wss_url(api_url, api_secret, api_key):
    """
    Generate auth params for API request.
    """
    api_host = urlparse(api_url).netloc
    api_path = urlparse(api_url).path

    # step1: generate signature
    rfc1123_date = generate_rfc1123_date()
    signature_origin = textwrap.dedent(f'''
        host: {api_host}
        date: {rfc1123_date}
        GET {api_path} HTTP/1.1
    ''').strip()
    signature_sha = hmac.new(
        api_secret.encode(),
        signature_origin.encode(),
        digestmod=hashlib.sha256
    ).digest()
    signature_sha_base64 = base64.b64encode(signature_sha).decode()

    # step2: generate authorization
    authorization_payload = {
        'api_key': api_key,
        'algorithm': 'hmac-sha256',
        'headers': 'host date request-line',
        'signature': signature_sha_base64
    }
    authorization_origin = ', '.join(f'{k}="{v}"' for k, v in authorization_payload.items())
    authorization = base64.b64encode(authorization_origin.encode()).decode()

    # step3: generate wss url
    payload = {
        'authorization': authorization,
        'date': rfc1123_date,
        'host': api_host
    }
    url = api_url + '?' + urlencode(payload)
    # print(f'wss url: {url}')
    return url
