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

import base

from metrium import quorum

SLEEP_TIME = 30.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor,
this bot uses a large value as its tick operation is
a lot expensive and should be used with care """

BASE_URL = "https://erp.startomni.com/"
""" The base url to be used to compose the various
complete url values for the various operations """

class OmniBot(base.Bot):

    def __init__(self, sleep_time = SLEEP_TIME, *args, **kwargs):
        base.Bot.__init__(self, sleep_time, *args, **kwargs)
        self.session_id = None

    def tick(self):
        if not self.session_id:
            username = quorum.conf("OMNIX_USERNAME")
            password = quorum.conf("OMNIX_PASSWORD")
            if username == None or password == None:
                raise RuntimeError("Missing authentication information")
            self.login(username, password)

        url = BASE_URL + "omni/sale_snapshots/stats.json"
        contents_s = self.get_json(url, unit = "day")

        for id in contents_s:
            url = BASE_URL + "omni/stores/%s.json" % id
            contents_s = self.get_json(url)
            print contents_s["name"]

        print contents_s

    def login(self, username, password):
        url = BASE_URL + "omni/login.json"
        contents_s = self.post_json(
            url,
            authenticate = False,
            username = username,
            password = password
        )
        self.session_id = contents_s["session_id"]

    def get_json(self, url, authenticate = True, token = False, **kwargs):
        if authenticate: kwargs["session_id"] = self.session_id
        try: data = quorum.get_json(url, **kwargs)
        except quorum.JsonError, error: self.handle_error(error)
        return data

    def post_json(self, url, authenticate = True, **kwargs):
        if authenticate: kwargs["session_id"] = self.session_id
        try: data = quorum.post_json(url, **kwargs)
        except quorum.JsonError, error: self.handle_error(error)
        return data

    def handle_error(self, error):
        data = error.get_data()
        exception = data.get("exception", {})
        exception_name = exception.get("exception_name", None)
        message = exception.get("message", None)
        if exception_name == "ControllerValidationReasonFailed":
            self.reset_session_id()
        elif exception_name:
            raise RuntimeError("%s - %s" % (exception_name, message))
