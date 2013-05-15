// Hive Metrium System
// Copyright (C) 2008-2012 Hive Solutions Lda.
//
// This file is part of Hive Metrium System.
//
// Hive Metrium System is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Hive Metrium System is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Hive Metrium System. If not, see <http://www.gnu.org/licenses/>.

// __author__    = João Magalhães <joamag@hive.pt>
// __version__   = 1.0.0
// __revision__  = $LastChangedRevision$
// __date__      = $LastChangedDate$
// __copyright__ = Copyright (c) 2010-2012 Hive Solutions Lda.
// __license__   = GNU General Public License (GPL), Version 3

jQuery(document).ready(function() {
            var pusher = new Pusher("73ce330c0a4efe4266a2");
            var global = pusher.subscribe("global");
            global.bind("message", function(data) {
                        alert("An event was triggered with message: " + data.contents);
                    });
        });
