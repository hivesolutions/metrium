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

(function(jQuery) {
    jQuery.fn.upusher = function(options) {
        var matchedObject = this;
        matchedObject.each(function() {
                    var element = jQuery(this);
                    var key = element.attr("data-key");
                    if (!key) {
                        return;
                    }

                    var pusher = new Pusher(key);
                    element.data("pusher", pusher);
                });
        return matchedObject;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.udashboard = function(options) {
        var matchedObject = this;
        var pusher = jQuery(".pusher", matchedObject);
        var status = jQuery(".status", matchedObject);

        var pusher = pusher.data("pusher");
        if (!pusher) {
            return matchedObject;
        }

        var initialize = function() {
            _start();
            _general();
        };

        var _start = function() {
            var connection = pusher.connection;
            var global = pusher.subscribe("global");
            matchedObject.data("global", global);

            connection.bind("connecting", function() {
                        status.html("connecting");
                        status.removeClass("valid");
                        status.addClass("invalid");
                    });

            connection.bind("connected", function() {
                        status.html("connected");
                        status.removeClass("invalid");
                        status.addClass("valid");
                    });

            connection.bind("unavailable", function() {
                        status.html("unavailable");
                        status.removeClass("valid");
                        status.addClass("invalid");
                    });

            connection.bind("disconnected", function() {
                        status.html("disconnected");
                        status.removeClass("valid");
                        status.addClass("invalid");
                    });

            connection.bind("error", function(error) {
                        status.html("error");
                        status.removeClass("valid");
                        status.addClass("invalid");
                    });
        };

        var _general = function() {
            var global = matchedObject.data("global");
            var message = jQuery(".message", matchedObject);

            global.bind("message", function(data) {
                        message.html(data.contents);
                    });
        };

        initialize();
        return matchedObject;
    };
})(jQuery);

jQuery(document).ready(function() {
            var pusher = jQuery(".pusher");
            pusher.upusher();

            var dashboard = jQuery(".dashboard");
            dashboard.udashboard();
        });
