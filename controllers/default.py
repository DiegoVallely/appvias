# -*- coding: utf-8 -*-
# /usr/bin/python

def index():

    form = SQLFORM.factory(
                Field('email', requires =[ IS_EMAIL(error_message='invalid email!'), IS_NOT_EMPTY() ]))
    form['_id'] = "email"
    form['_placeholder'] = "Email Address"
    form['_name'] = "email"
    if form.process().accepted:
        session.name = form.vars.name
        session.email = form.vars.email
        session.subject = form.vars.subject
        session.message = form.vars.message
        if mail:
            if mail.send(to=['otheremail@yahoo.com'],
                subject='project minerva',
                message= "Hello this is an email send from minerva.com from contact us form.\nName:" \
                            +session.name+" \nEmail : " + session.email +"\nSubject : "+session.subject +\
                            "\nMessage : "+ session.message+ ".\n "
            ):
                response.flash = 'email sent sucessfully.'
            else:
                response.flash = 'fail to send email sorry!'
        else:
            response.flash = 'Unable to send the email : email parameters not defined'
    elif form.errors:
            response.flash='form has errors.'

    return dict(form=form)


def contact():

    form = SQLFORM.factory(
                Field('name', requires=IS_NOT_EMPTY()),
                Field('email', requires =[ IS_EMAIL(error_message='invalid email!'), IS_NOT_EMPTY() ]),
                Field('subject', requires=IS_NOT_EMPTY()),
                Field('message', requires=IS_NOT_EMPTY(), type='text')
                )   
    if form.process().accepted:
        session.name = form.vars.name
        session.email = form.vars.email
        session.subject = form.vars.subject
        session.message = form.vars.message
        if mail:
            if mail.send(to=['otheremail@yahoo.com'],
                subject='project minerva',
                message= "Hello this is an email send from minerva.com from contact us form.\nName:"+ session.name+" \nEmail : " + session.email +"\nSubject : "+session.subject +"\nMessage : "+session.message+ ".\n "
            ):
                response.flash = 'email sent sucessfully.'
            else:
                response.flash = 'fail to send email sorry!'
        else:
            response.flash = 'Unable to send the email : email parameters not defined'
    elif form.errors:
            response.flash='form has errors.'

    return dict()

def elements():
    return dict()