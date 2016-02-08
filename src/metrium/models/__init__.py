#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Metrium System
# Copyright (c) 2008-2016 Hive Solutions Lda.
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

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from . import config
from . import account
from . import base
from . import conversation
from . import debug
from . import github
from . import log
from . import mail
from . import omni
from . import pending

from .config import Config, BasicConfig, GithubConfig, MailConfig, OmniConfig,\
    PendingConfig
from .account import Account
from .base import Base
from .conversation import Conversation
from .debug import Debug
from .github import Github
from .log import Log
from .mail import Mail
from .omni import Omni
from .pending import Pending
