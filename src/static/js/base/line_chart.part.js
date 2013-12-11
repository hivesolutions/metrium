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
