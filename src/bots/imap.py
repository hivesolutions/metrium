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

import time
import imaplib

import email.utils
import email.header

import models

import base

SLEEP_TIME = 60.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor,
this bot uses a large value as its tick operation is
a lot expensive and should be used with care """

class ImapBot(base.Bot):

    def __init__(self, sleep_time = SLEEP_TIME, *args, **kwargs):
        base.Bot.__init__(self, sleep_time, *args, **kwargs)

    def tick(self):
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login("joamag@gmail.com", "ek42Xuyw")
        imap.select("inbox")
        _result, data = imap.search(None, "ALL")

        ids = data[0]
        id_list = ids.split()
        id_list.reverse()

        for email_id in id_list:
            _result, data = imap.fetch(email_id, "(rfc822.size body[header.fields (date)])")
            date = data[0][1].lstrip("Date: ").strip() + " "
            date, charset = email.header.decode_header(date)[0]
            date = charset and date.decode(charset) or date
            date_tuple = email.utils.parsedate(date)
            timestamp = time.mktime(date_tuple)

            _result, data = imap.fetch(email_id, "(rfc822.size body[header.fields (subject)])")
            subject = data[0][1].lstrip("Subject: ").strip() + " "
            subject, charset = email.header.decode_header(subject)[0]
            subject = charset and subject.decode(charset) or subject

            mail = models.Mail()
            mail.date = timestamp
            mail.subject = subject
            mail.save()

        imap.logout()
