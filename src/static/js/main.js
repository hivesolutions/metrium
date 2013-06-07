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
            _layout();
            _general();
            _modules();
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

        var _layout = function() {
            var _html = jQuery("html");
            _html.css("overflow-y", "auto");
        };

        var _general = function() {
            jQuery.ajax({
                        url : "/state",
                        beforeSend : function() {
                            _hide();
                        },
                        success : function(data) {
                            _onState(data);
                            _show();
                        },
                        error : function() {
                            _show();
                        }
                    });
        };

        var _hide = function() {
            matchedObject.css("visibility", "hidden");
        };

        var _show = function() {
            matchedObject.css("visibility", "visible");
        };

        var _onState = function(state) {
            var global = matchedObject.data("global");
            for (var module in state) {
                var events = state[module];

                for (var name in events) {
                    var event = events[name];
                    for (var index = event.length - 1; index >= 0; index--) {
                        var instance = event[index];
                        var _event = {
                            contents : instance
                        };
                        global.emit(name, _event);
                    }
                }
            }
        };

        var _modules = function() {
            matchedObject.udate();
            matchedObject.ulog();
        };

        initialize();
        return matchedObject;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.udate = function(options) {

        var TIMEOUT = 10000;

        var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Starturday"];
        var DAYS_PT = ["Domnigo", "Segunda-feira", "Terça-Feira",
                "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"];

        var MONTHS = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November",
                "December"];
        var MONTHS_PT = ["Janeiro", "Febreiro", "Março", "Abril", "Maio",
                "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro",
                "Dezembro"];

        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            _update();
            setInterval(function() {
                        _update();
                    }, TIMEOUT);
        };

        var _update = function() {
            var date = jQuery(".date", matchedObject);
            var weekDay = jQuery(".week-day", date);
            var day = jQuery(".day", date);
            var time = jQuery(".time", date);

            var _date = new Date();
            var dayIndex = _date.getDay();
            var dayString = DAYS_PT[dayIndex];

            var dayMonth = _date.getDate();
            var dayMonthS = _toString(dayMonth);
            var month = _date.getMonth();
            var monthS = MONTHS_PT[month];
            var dayLine = dayMonthS + " " + monthS;

            var hours = _date.getHours();
            var minutes = _date.getMinutes();
            var timeLine = _toString(hours) + ":" + _toString(minutes);

            weekDay.html(dayString);
            day.html(dayLine);
            time.html(timeLine);
        };

        var _toString = function(value, length) {
            length = length || 2;
            value = String(value);

            for (var index = value.length; index < length; index++) {
                value = "0" + value;
            }
            return value;
        };

        initialize();
        return matchedObject;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.ulog = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("log.message", function(data) {
                        _new(data.contents);
                    });
        };

        var _new = function(contents) {
            var date = new Date();
            var hours = date.getHours();
            var minutes = date.getMinutes();
            var timeLine = contents.time || _toString(hours) + ":"
                    + _toString(minutes);

            var context = jQuery(".context", matchedObject);
            var news = jQuery(".news", context);
            var item = "<div class=\"news-item\">" + "<div class=\"title\">"
                    + "<span class=\"time\">" + timeLine + "</span>"
                    + "<span class=\"message\">" + contents.owner + "</span>"
                    + "<span class=\"marker " + contents.type + "\"></span>"
                    + "</div>" + "<div class=\"message\">" + contents.message
                    + "</div>" + "</div>";
            news.prepend(item);

            var newsElement = news[0];

            while (true) {
                var overflows = newsElement.scrollHeight > newsElement.clientHeight;
                if (!overflows) {
                    break;
                }

                var lastChild = jQuery("> :last-child", news);
                lastChild.remove();
            }
        };

        var _toString = function(value, length) {
            length = length || 2;
            value = String(value);

            for (var index = value.length; index < length; index++) {
                value = "0" + value;
            }
            return value;
        };

        initialize();
        return matchedObject;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.uprogress = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            if (matchedObject.length == 0) {
                return;
            }

            var width = matchedObject.width();
            var height = matchedObject.height();

            matchedObject.attr("width", width);
            matchedObject.attr("height", height);

            var value = matchedObject.attr("data-value");
            var target = matchedObject.attr("data-target");

            value = parseInt(value);
            target = target ? parseInt(target) : null;

            var valueP = value * 2.0 / 100.0;
            var targetP = target ? (target - value) * 2.0 / 100.0 : 0.0;
            var remainingP = 2.0 - targetP - valueP;

            var canvas = matchedObject[0];
            var context = canvas.getContext("2d");

            var centerX = canvas.width / 2;
            var centerY = canvas.height / 2;
            var lower = canvas.width > canvas.height
                    ? canvas.height
                    : canvas.width;
            var radius = (lower / 2) - 18;

            context.translate(centerX, centerY);
            context.rotate(Math.PI / 2 * -1);

            context.beginPath();
            context.arc(0, 0, radius, 0, valueP * Math.PI, false);
            context.lineWidth = 12;
            context.strokeStyle = "#d6de23";
            context.stroke();
            context.rotate(valueP * Math.PI);

            if (target) {
                context.beginPath();
                context.arc(0, 0, radius, 0, targetP * Math.PI, false);
                context.lineWidth = 12;
                context.strokeStyle = "#ee4036";
                context.stroke();
                context.rotate(targetP * Math.PI);
            }

            context.beginPath();
            context.arc(0, 0, radius, 0, remainingP * Math.PI, false);
            context.lineWidth = 12;
            context.strokeStyle = "rgba(255, 255, 255, 0.6)";
            context.stroke();
        };

        initialize();
        return matchedObject;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.ulinechart = function(options) {
        var PADDING_TOP = 32;
        var PADDING_LEFT = 5;
        var PADDING_RIGHT = 5;

        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            if (matchedObject.length == 0) {
                return;
            }

            var width = matchedObject.width();
            var height = matchedObject.height();

            matchedObject.attr("width", width);
            matchedObject.attr("height", height);

            var values = [100, 120, 80, 20, 45, 67, 23];
            var maxValue = 0;

            for (var index = 0; index < values.length; index++) {
                var value = values[index];
                maxValue = value > maxValue ? value : maxValue;
            }

            var canvas = matchedObject[0];
            var context = canvas.getContext("2d");

            var widthChart = canvas.width - PADDING_LEFT - PADDING_RIGHT;
            var heightChart = canvas.height - PADDING_TOP;
            var stepWidth = widthChart / (values.length - 1);
            var xPosition = PADDING_LEFT;

            for (var index = 0; index < values.length; index++) {
                var value = values[index];
                var yPosition = canvas.height
                        - (value * heightChart / maxValue);

                if (index != 0) {
                    context.beginPath();
                    context.strokeStyle = "#ffffff";
                    context.moveTo(xPositionP, yPositionP);
                    context.lineTo(xPosition, yPosition);
                    context.lineWidth = 4;
                    context.stroke();

                    context.beginPath();
                    context.fillStyle = "rgba(255, 255, 255, 0.2)";
                    context.moveTo(xPositionP, yPositionP);
                    context.lineTo(xPosition, yPosition);
                    context.lineTo(xPosition, canvas.height);
                    context.lineTo(xPositionP, canvas.height);
                    context.closePath();
                    context.fill();
                }

                if (index != 0 && index != values.length - 1) {
                    context.beginPath();
                    context.strokeStyle = "rgba(255, 255, 255, 0.3)";
                    context.lineWidth = 2;
                    context.dashedLine(xPosition, yPosition, xPosition,
                            canvas.height, [6, 4]);
                    context.stroke();
                }

                context.beginPath();
                context.fillStyle = "#ffffff";
                context.arc(xPosition, yPosition, 5, 0, 2 * Math.PI, false);
                context.fill();

                var xPositionP = xPosition;
                var yPositionP = yPosition;

                xPosition += stepWidth;
            }
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

            var progress = jQuery(".progress");
            progress.uprogress();

            var lineChart = jQuery(".line-chart");
            lineChart.ulinechart();
        });
