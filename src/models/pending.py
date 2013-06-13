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

import hashlib

import quorum

import base
import conversation

class Pending(base.Base):

    priority = dict(
        index = True,
        type = int
    )

    severity = dict(
        index = True
    )

    pre = dict(
        index = True
    )

    description = dict(
        index = True
    )

    author = dict(
        index = True
    )

    conversation = dict(
        type = quorum.reference(
            conversation.Conversation,
            name = "id"
        )
    )

    @classmethod
    def validate_new(cls):
        return super(Pending, cls).validate_new() + [
            quorum.not_null("priority"),

            quorum.not_null("severity"),
            quorum.not_empty("severity"),

            quorum.not_null("pre"),
            quorum.not_empty("pre"),

            quorum.not_null("description"),
            quorum.not_empty("description")
        ]

    @classmethod
    def reset(cls):
        pendings = cls.find()
        for pending in pendings: pending.delete()

    @classmethod
    def get_state(cls):
        events = cls.get_events()
        return {
            "pending.update" : [{
                "pendings" : events
            }]
        }

    @classmethod
    def get_events(cls, count = 10):
        pendings = cls.find(sort = [("priority", 1)], limit = count)
        return [pending.get_event() for pending in pendings]

    @classmethod
    def get_signature(cls, count = 10):
        signature = hashlib.sha256()
        pendings = cls.find(sort = [("priority", 1)], limit = count)
        for pending in pendings:
            buffer = pending.get_buffer()
            signature.update(buffer)
        return signature.hexdigest()

    def get_event(self):
        return {
            "priority" : self.priority,
            "severity" : self.severity,
            "pre" : self.pre,
            "description" : self.description,
            "author" : self.author
        }

    def get_buffer(self):
        return str(self.priority) + self.pre + self.description + self.author