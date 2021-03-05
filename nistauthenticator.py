from tornado import gen
from traitlets import Unicode
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
        user = self.user_from_username(username)
        self.set_login_cookie(user)
        self._jupyterhub_user = user

        self.redirect(self.get_next_url(user))

class NISTLogoutHandler(LogoutHandler):
    async def render_logout_page(self):
        self.redirect(self.authenticator.logoutURL)

class NISTAuthenticator(Authenticator):
    logoutURL = Unicode(
            default_value='https://www.google.com/',
            config=True,
            help="""
            URL to redirect to when hub user logs out.
            """
    )

    def get_handlers(self,app):
        '''Register our own customized login handler in JupyterHub'''
        return [
                (r'/login', NISTLoginHandler),
                (r'/logout', NISTLogoutHandler)
                ]

    @gen.coroutine
    def authenticate(self, *args):
        raise NotImplementedError()
