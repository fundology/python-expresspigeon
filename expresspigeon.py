import urllib2
import simplejson


class ExpressPigeonException(Exception):
    pass


class ExpressPigeonWarning(Warning):
    pass


class Connection(object):
    """
    Express pigeon api connection
    """

    def __init__(self, apikey='', proto='https'):
        self._apikey = apikey
        api_host = 'api.expresspigeon.com'
        self.url = '%s://%s/' % (proto, api_host)

    def _api_call(self,
                  suburl='',
                  method='',
                  format='json',
                  contenttype=False,
                  params=None):
        url = self.url + suburl
        req = urllib2.Request(url)
        req.add_header('X-auth-key', self._apikey)
        if contenttype:
            req.add_header('Content-Type', 'application/%s' % (format))
        if method == 'post':
            r = ''
            for k, v in params.items():
                r += '"%s": "%s",' % (k, v)
            params = '{%s}' % r[:-1]
            req.add_data(params)
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        result = simplejson.loads(data)
        return result

    def get_list(self):
        """
        Show all list
        Url:
        https://api.expresspigeon.com/lists
        """
        return self._api_call(suburl='lists',
                              method='get')

    def create_list(self, params, format='json'):
        """
        Create new list
        Url:
        https://api.expresspigeon.com/lists
        """
        return self._api_call(suburl='lists',
                              method='post',
                              contenttype=True,
                              params=params,
                              format=format)

    def create_contact(self, params, format='json'):
        """
        Create campaign
        Url:
        https://api.expresspigeon.com/contacts
        """
        return self._api_call(suburl='contacts',
                              method='post',
                              contenttype=True,
                              params=params,
                              format=format)
