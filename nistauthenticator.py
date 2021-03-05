from tornado import gen
from jupyterhub.auth import Authenticator
from jupyterhub.handlers.base import BaseHandler
from jupyterhub.handlers.login import LogoutHandler
from jupyterhub.utils import url_path_join

class NISTLoginHandler(BaseHandler):
    async def get(self):
        # retrive experimenter ID
        username = self.request.headers['X-Authorized-User']

        # create and register user in hub db if first time login
        # retrieve user info for setting cookie and redirect
        user = self.user_from_username(username);
        self.set_login_cookie(user);
        self._jupyterhub_user = user

        self.redirect(self.get_next_url(user))
        #_url = url_path_join(self.hub.server.base_url, 'home')
        #self.redirect(_url)

class NISTLogoutHandler(LogoutHandler):
    async def render_logout_page(self):
        # html = await self.render_template('logout.html')
        # self.finish(html)

        self.redirect('https://google.com/')

class NISTAuthenticator(Authenticator):
    def login_url(self, base_url):
        return url_path_join(base_url, 'nist_login')

    def get_handlers(self,app):
        '''Register our own customized login handler in JupyterHub'''
        return [
                (r'/login', NISTLoginHandler),
                (r'/logout', NISTLogoutHandler)
                ]

    @gen.coroutine
    def authenticate(self, *args):
        raise NotImplementedError()