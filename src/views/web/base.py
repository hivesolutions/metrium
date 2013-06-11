#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Metrium System
# Copyright (C) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Metrium System.
#
# Hive Metrium System is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Metrium System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Metrium System. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import models

from metrium import app
from metrium import flask
from metrium import quorum

@app.context_processor
def utility_processor():
    return dict(acl = quorum.check_login)

@app.route("/", methods = ("GET",))
@app.route("/index", methods = ("GET",))
@quorum.ensure("index")
def index():
    return flask.render_template(
        "index.html.tpl",
        link = "home"
    )

@app.route("/about", methods = ("GET",))
@quorum.ensure("about")
def about():
    return flask.render_template(
        "about.html.tpl",
        link = "about"
    )

@app.route("/signin", methods = ("GET",))
def signin():
    return flask.render_template(
        "signin.html.tpl"
    )

@app.route("/signin", methods = ("POST",))
def login():
    # retrieves the username and the password fields
    # and uses them to run the login logic raising an
    # error in case an invalid authentication occurs
    username = quorum.get_field("username")
    password = quorum.get_field("password")
    try: account = models.Account.login(username, password)
    except quorum.OperationalError, error:
        return flask.render_template(
            "signin.html.tpl",
            username = username,
            error = error.message
        )

    # updates the current user (name) in session with
    # the username that has just be accepted in the login
    flask.session["username"] = account.username
    flask.session["tokens"] = account.tokens
    flask.session["acl"] = quorum.check_login

    # makes the current session permanent this will allow
    # the session to persist along multiple browser initialization
    flask.session.permanent = True

    return flask.redirect(
        flask.url_for("index")
    )

@app.route("/signout", methods = ("GET", "POST"))
def logout():
    if "username" in flask.session: del flask.session["username"]
    if "tokens" in flask.session: del flask.session["tokens"]

    return flask.redirect(
        flask.url_for("signin")
    )

@app.route("/state", methods = ("GET",), json = True)
@quorum.ensure("state", json = True)
def state():
    log_state = models.Log.get_state()

    state = dict(
        log = log_state
    )
    return state

@app.route("/dashboard", methods = ("GET",))
@quorum.ensure("dashboard")
def dashboard():
    return flask.render_template(
        "dashboard.html.tpl"
    )

@app.route("/video", methods = ("GET",))
@quorum.ensure("video")
def video():
    url = quorum.get_field("url")

    pusher = quorum.get_pusher()
    pusher["global"].trigger("video.open", {
        "url" : url
    })

    return flask.redirect(
        flask.url_for("index")
    )
