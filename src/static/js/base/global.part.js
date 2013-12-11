(function(jQuery) {
    jQuery.fn.uglobal = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("omni.top_stores", function(data) {
                        console.info(data);
                    });
        };

        initialize();
        return matchedObject;
    };
})(jQuery);
