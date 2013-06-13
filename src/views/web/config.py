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

@app.route("/config", methods = ("GET",))
@quorum.ensure("config.base")
def base_config():
    return flask.render_template(
        "config/base.html.tpl",
        link = "config",
        sub_link = "base"
    )

@app.route("/config/mail", methods = ("GET",))
@quorum.ensure("config.mail")
def mail_config():
    config = models.MailConfig.get(raise_e = False) or {}
    return flask.render_template(
        "config/mail.html.tpl",
        link = "config",
        sub_link = "mail",
        config = config,
        errors = {}
    )

@app.route("/config/mail", methods = ("POST",))
@quorum.ensure("config.mail")
def do_mail_config():
    account = models.MailConfig.singleton()
    try: account.save()
    except quorum.ValidationError, error:
        return flask.render_template(
            "config/mail.html.tpl",
            link = "config",
            sub_link = "mail",
            config = error.model,
            errors = error.errors
        )

    # redirects the user to the overall configuration
    # selection, as this is the default behavior
    return flask.redirect(
        flask.url_for("base_config")
    )
