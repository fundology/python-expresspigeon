import urllib
import urllib2
import simplejson


class ExpressPigeonError(Exception):
    """
    Exception error for expresspigeon
    """
    def __init__(self, type, message):
        Exception.__init__(self, message)
        self.type = type


class Connection(object):
    """
    Express pigeon api connection
    """

    def __init__(self, apikey='', proto='https'):
        self._apikey = apikey
        api_host = 'api.expresspigeon.com'
        self.url = '%s://%s' % (proto, api_host)

    def _api_call(self,
                  id='',
                  suburl='',
                  nest_url='',
                  method='',
                  format='json',
                  contenttype=False,
                  params=None,
                  url_params=None):
        try:
            url = self.url
            if id:
            #  combine url and id
                if suburl == 'contacts':
                    nest_url = 'list'
                url = '%s/%s/%s' % (url, nest_url, id)
            url = '%s/%s' % (url, suburl)
            print url
            if url_params:
                url = '%s?%s' % (url, urllib.urlencode(url_params))
            req = urllib2.Request(url)
            req.add_header('X-auth-key', self._apikey)
            if contenttype:
                req.add_header('Content-Type', 'application/%s' % (format))
            if params:
                r = ''
                for k, v in params.items():
                    # if there's a child dictionary
                    if k == 'contact':
                        r1 = ''
                        for k1, v1 in v.items():
                            r1 += '"%s": "%s",' % (k1, v1)
                        r += '"%s": {%s},' % (k, r1[:-1])
                    else:
                        r += '"%s": "%s",' % (k, v)
                params = '{%s}' % r[:-1]
                req.add_data(params)
            if method:
                req.get_method = lambda: method
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            result = simplejson.loads(data)
            return result
        except Exception, e:
            raise ExpressPigeonError(str(e))

    def get_list(self):
        """
        Show all list
        Url:
        https://api.expresspigeon.com/lists
        """
        return self._api_call(suburl='lists')

    def create_list(self, params, format='json'):
        """
        Create new list
        Url:
        https://api.expresspigeon.com/lists
        """
        return self._api_call(suburl='lists',
                              method='POST',
                              contenttype=True,
                              params=params,
                              format=format)

    def update_list(self, params, format='json'):
        """
        Update existing list
        """
        return self._api_call(suburl='lists',
                              method='PUT',
                              contenttype=True,
                              params=params,
                              format=format)

    def delete_list(self, id, format='json'):
        """
        Delete a list
        """
        return self._api_call(nest_url='lists',
                            id=id,
                            method='DELETE',
                            format=format)


    def create_update_contact(self, params, format='json'):
        """
        Create contacts
        Url:
        https://api.expresspigeon.com/contacts
        """
        return self._api_call(suburl='contacts',
                              method='POST',
                              contenttype=True,
                              params=params,
                              format=format)

    def get_contacts_list(self,
                          id,
                          url_params,
                          format='json'):
        """
        TODO:
        Display the contacts from a list
        https://api.expresspigeon.com/list/{list_id}/contacts
        """
        return self._api_call(suburl='contacts',
                              id=id,
                              url_params=url_params,
                              format=format)

    def read_single_contact_by_email(self,
                                     url_params, format='json'):
        """
        Read the email information
        """
        return self._api_call(suburl='contacts',
                               url_params=url_params,
                               format=format)

    def create_campaign(self, id, params, format='json'):
        """
        User create campaign
        """
        return self._api_call(suburl='campaigns',
                            method='POST',
                            contenttype=True,
                            params=params,
                            format=format)

    def delete_single_contact(self,
                              url_params,
                              suburl='contacts',
                              format='json'):
        """
        Delete single contact
        """
        return self._api_call(suburl='contacts',
                            url_params=url_params,
                            method="DELETE",
                            format=format)