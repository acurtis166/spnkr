""""""

from halo_infinite_api import util
from halo_infinite_api.api.authorities import base
from halo_infinite_api.api.authorities.iugcsessionfiles import models


class iugcsessionfilesAuthority(base.BaseAuthority):

    URL = 'https://s3infiniteugcsessions.blob.core.windows.net:443'
    AUTHENTICATION_METHODS = [None]
    SCHEME = 'Https'

    def getsessionblob(self):
        url = self.URL + ''
        params = ''
        resp = self._session.get(url, params=params)

