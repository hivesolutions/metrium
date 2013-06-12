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

import datetime

import models

import base

from metrium import quorum

SLEEP_TIME = 20.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor """

class PendingBot(base.Bot):

    def __init__(self, sleep_time = SLEEP_TIME, *args, **kwargs):
        base.Bot.__init__(self, sleep_time, *args, **kwargs)

    def tick(self):
        pendings = self.get_pendings()
        pusher = quorum.get_pusher()
        pusher["global"].trigger("pending.update", {
            "pendings" : pendings
        })

    def get_pendings(self, count = 10):
        folders = ["Pessoal", "inbox"] #@todo this is hardcoded, need configuration
        pendings = []

        for folder in folders:
            remaining = count - len(pendings)
            mails = models.Mail.find(limit = remaining, sort = [("date", 1)], folder = folder)
            
            for mail in mails:
                date = datetime.datetime.utcfromtimestamp(mail.date)
                date_s = date.strftime("%d/%m")

                pendings.append(dict(
                    severity = "urgent",   #@todo: this is hardcoded
                    pre = date_s,
                    description = mail.subject,
                    author = "unknown" #@todo: this is hardcoded
                ))

        return pendings