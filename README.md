# NISTAuthenticator
With NISTAuthenticator, you can authenticate JupyterHub users using a customized HTTP header.

## Use Case
This may come handy if you wish to integrate JupyterHub into a system with an existing authentication system.

We can put JupyterHub behind a reverse HTTP proxy and use an authentication middleware that re-directs hub users to the system's login page. Upon successful login, the reverse HTTP proxy adds to the original request a customized HTTP header with value set to the user ID. It then forwards the request to JupyterHub and NISTAuthenticator will authenticate the user via the HTTP header and perform all the necessary actions for subsequent requests to JupyterHub and user's single-user notebook server to work.

## Installation
You can install with pip:

```bash
pip install nistauthenticator
```

## Usage
After successful installation, you can use `nistauthenticator` as the authenticator for JupyterHub by including the following in your JupyterHub configuration file:

```py
c.JupyterHub.authenticator_class = 'nistauthenticator.NISTAuthenticator'
```

In the same JupyterHub configuration file, you can configure the name of HTTP header to use for authentication via

```
c.NISTAuthenticator.user_header = 'your-http-header-name'
```

and the logout URL can be specified via

```py
c.NISTAuthenticator.logoutURL = 'your-logout-url'
```
