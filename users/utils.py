from oauthlib.oauth1 import Client


CONSUMER_KEY = 'warwickcatulator.co.uk'
CONSUMER_SECRET = 'TGVhdmUgdGhlIGtleSB0eXBlIyZXQu'

class CustomClient(Client):
    def _render(self, request, formencode=False, realm=None):
        request.headers["User-Agent"] = "A useful user agent for ITS"
        return super()._render(request, formencode, realm)