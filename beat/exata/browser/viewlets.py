from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets import common

from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize

class MenuViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/menu.pt')

class RodapeViewlet(ViewletBase):

    def login_name(self):
        auth = self.auth()
        name = None
        if auth is not None:
            name = getattr(auth, 'name_cookie', None)
        if not name:
            name = '__ac_name'
        return name

    def login_password(self):
        auth = self.auth()
        passwd = None
        if auth is not None:
            passwd = getattr(auth, 'pw_cookie', None)
        if not passwd:
            passwd = '__ac_password'
        return passwd

    def login_form(self):
        return '%s/login_form' % self.portal_state.portal_url()

    @memoize
    def auth(self, _marker=[]):
        acl_users = getToolByName(self.context, 'acl_users')
        return getattr(acl_users, 'credentials_cookie_auth', None)

    index = ViewPageTemplateFile('templates/rodape.pt')

class SearchBoxViewlet(common.SearchBoxViewlet):
    index = ViewPageTemplateFile('templates/busca.pt')

class PathBarViewlet(common.PathBarViewlet):
    index = ViewPageTemplateFile('templates/path_bar.pt')
