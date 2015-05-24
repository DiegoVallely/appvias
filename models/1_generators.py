# -*- coding: utf-8 -*-
from gluon.custom_import import track_changes
track_changes(True)

from gluon.contrib.markdown.markdown2 import markdown
from gluon.tools import Auth, Service, Crud

# from helpers.mail import Mailer

service = Service()
private_service = Service()

# generator for database connection
db = DAL(**config.db)
crud = Crud(db)


# Initialize Mail
mail = Mailer()

# the settings for model and auth
auth = Auth(db, hmac_key=Auth.get_or_create_key())
auth.settings.formstyle = config.auth.settings.formstyle
auth.settings.extra_fields['auth_user'] = \
	config.auth.settings.extra_fields.auth_user
# auth.settings.mailer = mail
auth.settings.registration_requires_verification = \
	config.auth.settings.registration_requires_verification
auth.settings.registration_requires_approval = \
	config.auth.settings.registration_requires_approval
auth.settings.login_after_registration = \
	config.auth.settings.login_after_registration
auth.settings.logged_url = config.auth.settings.logged_url
auth.settings.login_next = config.auth.settings.login_next
auth.settings.register_next = config.auth.settings.register_next
# auth.messages.registration_successful = \
	# config.auth.messages.registration_successful


register on accept
auth.settings.register_onaccept = \
	lambda form: mail.my_mail_sender(template="Bem Vindo",
									context=form.vars,
									to=form.vars.email,
									subject="Bem Vindo ao PathRider")

auth.define_tables()

User = db.auth_user
me, a0, a1 = auth.user_id, request.args(0), request.args(1)
alphabetical = User.first_name|User.last_name

def name_of(user):
	return '%(first_name)s %(last_name)s' % user