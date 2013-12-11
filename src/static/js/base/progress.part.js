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

            var widthS = matchedObject.attr("width");
            var heightS = matchedObject.attr("height");

            var _width = parseInt(widthS);
            var _height = parseInt(heightS);

            if(width && width != _width) {
                _width = width;
                matchedObject.attr("width", width);
            }

            if(height && height != _height) {
                _height = height;
                matchedObject.attr("height", height);
            }

            width = _width;
            height = _height;

            var value = matchedObject.attr("data-value");
            var target = matchedObject.attr("data-target");

            value = parseInt(value);
            target = target ? parseInt(target) : null;

            var valueP = value * 2.0 / 100.0;
            var targetP = target ? (target - value) * 2.0 / 100.0 : 0.0;
            var remainingP = 2.0 - targetP - valueP;

            var canvas = matchedObject[0];
            var context = canvas.getContext("2d");
            context.setTransform(1, 0, 0, 1, 0, 0);
            context.clearRect(0, 0, width, height);

            var centerX = width / 2;
            var centerY = height / 2;
            var lower = width > height ? height : width;
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
