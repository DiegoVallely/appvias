# -*- coding:utf-8 -*-

from gluon.storage import Storage

config = Storage(db=Storage(),
	auth=Storage(settings=Storage(extra_fields=Storage()),
		message=Storage()),
	mail=Storage())

# The database connection
config.db.uri = "sqlite://appdb.sqlite"
# Check reserved
config.db.check_reserved = ['all']


# config.auth
config.auth.settings.formstyle = "divs"
config.auth.settings.registration_requires_verification = False
config.auth.settings.registration_requires_approval = False
config.auth.settings.login_after_registration = False
config.auth.settings.logged_url = URL('user','perfil')
config.auth.settings.login_next = URL('user','perfil')
config.auth.settings.register_next = URL('user','perfil')
# config.auth.messages.logged_in = 'Logged in'
# config.auth.messages.registration_successful = 'Registration successful'

config.auth.settings.extra_fields.auth_user = [
	Field("endereco"),
	Field("cep"),
	Field("cidade"),
	Field("estado"),
	Field("avatar", "upload"),
	Field("thumbnail", "upload")]


# mail
config.mail.server = "smtp.gmail.com:465"
config.mail.sender = "appvias.br@gmail.com"
config.mail.login = "@appvias:appvias123"



# initialize current
from gluon import current
current.config = config