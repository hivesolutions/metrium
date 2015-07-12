#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Metrium System
# Copyright (C) 2008-2015 Hive Solutions Lda.
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

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import quorum

from metrium import models

from . import base

SLEEP_TIME = 60.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor,
this bot uses a large value as its tick operation is
a lot expensive and should be used with care """

class GithubBot(base.Bot):

    def __init__(self, sleep_time = SLEEP_TIME, *args, **kwargs):
        base.Bot.__init__(self, sleep_time, *args, **kwargs)

    def tick(self):
        api = models.OmniConfig.get_api()

        self.register_callback(api)
        top_commiters = self.top_commiters(api)

        #_omni = models.Omni.get(raise_e = False)
        #if not _omni: _omni = models.Omni()
        #_omni.sales_total = sales_total
        #_omni.sales_data = sales_data
        #_omni.sales_stores = sales_stores
        #_omni.entries_stores = entries_stores
        #_omni.top_stores = top_stores
        #_omni.top_employees = top_employees
        #_omni.save()

        #pusher = quorum.get_pusher()
        #pusher.trigger("global", "omni.sales_total", {
        #    "sales_total" : sales_total
        #})
        #pusher.trigger("global", "omni.sales_data", {
        #    "sales_data" : sales_data
        #})
        #pusher.trigger("global", "omni.sales_stores", {
        #    "sales_stores" : sales_stores
        #})
        #pusher.trigger("global", "omni.entries_stores", {
        #    "entries_stores" : entries_stores
        #})
        #pusher.trigger("global", "omni.top_stores", {
        #    "top_stores" : top_stores
        #})
        #pusher.trigger("global", "omni.top_employees", {
        #    "top_employees" : top_employees
        #})

    def commits_total(self, api):
        stats = api.stats_sales(span = 2, has_global = True)
        _global = stats["-1"]
        sales_total = _global["net_price_vat"]
        return sales_total

    def commits_repo(self, api):
        sales_stores = []

        stats = api.stats_sales(span = 2)
        for _object_id, values in stats.items():
            name = values["name"]
            net_price_vat = values["net_price_vat"]
            current = net_price_vat[-1]
            previous = net_price_vat[-2]
            tuple = (current, previous, name)
            sales_stores.append(tuple)

        sales_stores.sort(reverse = True)
        return sales_stores

    def top_repos(self, api):
        top_stores = []

        stats = api.stats_sales(span = 1)
        for _object_id, values in stats.items():
            name = values["name"]
            number_sales = values["number_sales"]
            current = number_sales[-1]
            tuple = (current, name)
            top_stores.append(tuple)

        top_stores.sort(reverse = True)
        return top_stores

    def top_commiters(self, api):
        top_employees = []

        stats = api.stats_employee(unit = "month", span = 1, has_global = True)
        for object_id, values in stats.items():
            values = values["-1"]
            employee = values["employee"]
            amount_price_vat = values["amount_price_vat"]
            number_sales = values["number_sales"]
            current_amount = amount_price_vat[-1]
            current_number = number_sales[-1]
            media = api.info_media_entity(int(object_id), dimensions = "64x64")
            image_url = api.base_url + "omni/media/" + media[0]["secret"] if media else None
            tuple = (current_amount, current_number, employee, image_url)
            top_employees.append(tuple)

        top_employees.sort(reverse = True)
        return top_employees
