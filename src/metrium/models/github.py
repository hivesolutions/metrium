#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Metrium System
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Metrium System.
#
# Hive Metrium System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Metrium System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Metrium System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from . import base

class Github(base.Base):

    commits_total = dict(
        type = list
    )

    commits_data = dict(
        type = list
    )

    issues_users = dict(
        type = list
    )

    commits_users = dict(
        type = list
    )

    @classmethod
    def get_state(cls):
        omni = cls.get(raise_e = False)
        if not omni: return dict()
        return {
            "github.commits_total" : [{
                "commits_total" : omni.commits_total
            }],
            "github.commits_data" : [{
                "commits_data" : omni.commits_data
            }],
            "github.issues_users" : [{
                "issues_users" : omni.issues_users
            }],
            "github.commits_users" : [{
                "commits_users" : omni.commits_users
            }]
        }
