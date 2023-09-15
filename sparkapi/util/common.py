from datetime import datetime
from email.utils import formatdate


def generate_rfc1123_date():
    """
    Generate a RFC 1123 compliant date string.

    """
    current_datetime = datetime.now()
    timestamp = current_datetime.timestamp()
    return formatdate(timeval=timestamp, localtime=False, usegmt=True)

    # the same as:
    # datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S %Z')
