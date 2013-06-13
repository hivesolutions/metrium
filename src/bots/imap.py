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

SLEEP_TIME = 30.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor,
this bot uses a large value as its tick operation is
a lot expensive and should be used with care """

class ImapBot(base.Bot):

    def __init__(self, sleep_time = SLEEP_TIME, *args, **kwargs):
        base.Bot.__init__(self, sleep_time, *args, **kwargs)

    def tick(self):
        imap = self.get_imap()

        try:
            self.update_folder(imap, folder = "inbox")
            self.update_folder(imap, folder = "Pessoal")
        finally:
            imap.logout()

    def get_imap(self):
        config = models.MailConfig.get()
        imap = imaplib.IMAP4_SSL(config.host)
        imap.login(config.username, config.password)
        return imap

    def update_folder(self, imap, folder = "inbox", limit = -1):
        result, data = imap.select(folder, readonly = True)
        if not result == "OK": return

        try:
            result, data = imap.uid("SEARCH", "1:*")
            if not result == "OK": return

            ids = data[0]
            id_list = ids.split()
            id_list.reverse()

            if not limit == -1: id_list = id_list[:limit]
            self.sync_folder(imap, id_list, folder)
        finally:
            imap.close()

    def sync_folder(self, imap, id_list, folder):
        mails = models.Mail.find(folder = folder)

        for mail in mails:
            if mail.uid in id_list: continue
            mail.delete()

        for mail_id in id_list:
            self.save_mail(imap, mail_id, folder)

    def save_mail(self, imap, mail_id, folder):
        mail = models.Mail.find(uid = mail_id)
        if mail: return

        _result, data = imap.uid("FETCH", mail_id, "(rfc822)")
        contents = data[0][1]
        message = email.message_from_string(contents)

        message_id = message.get("message-id", None)
        message_id, charset = email.header.decode_header(message_id)[0]
        message_id = charset and message_id.decode(charset) or message_id

        _from = message.get("from", None)
        _from, charset = email.header.decode_header(_from)[0]
        _from = charset and _from.decode(charset) or _from
        sender_extra, sender = email.utils.parseaddr(_from)

        date = message.get("date", None)
        date, charset = email.header.decode_header(date)[0]
        date = charset and date.decode(charset) or date
        date_tuple = email.utils.parsedate(date)
        timestamp = time.mktime(date_tuple)

        subject = message.get("subject", None)
        subject, charset = email.header.decode_header(subject)[0]
        subject = charset and subject.decode(charset) or subject

        mail = models.Mail.find(message_id = message_id)
        if mail: return

        mail = models.Mail()
        mail.uid = mail_id
        mail.message_id = message_id
        mail.sender = sender
        mail.sender_extra = sender_extra
        mail.folder = folder
        mail.date = timestamp
        mail.subject = subject
        mail.save()
