(function(jQuery) {
    jQuery.fn.uglobal = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("omni.sales_stores", function(data) {
                        _updateSalesStores(data.sales_stores);
                    });
            global.bind("omni.top_stores", function(data) {
                        _updateTopStores(data.top_stores);
                    });
        };

        var _updateSalesStores = function(salesStores, marker) {
            var _salesStores = jQuery(".sales-stores", matchedObject);
            var tableBody = jQuery("table > tbody", _salesStores);
            tableBody.empty();

            var size = salesStores.length > 5 ? 5 : salesStores.length;

            for (var index = 0; index < size; index++) {
                var item = salesStores[index];
                var current = item[0].toFixed(2);
                var previous = item[1].toFixed(2);
                var name = item[2];
                var row = jQuery("<tr>" + "<td>" + name + "</td>"
                        + "<td class=\"value\">" + previous + "</td>"
                        + "<td class=\"value\">" + current + "</td>" + "</tr>");
                if (marker) {
                    row.append("<td class=\"marker\">"
                            + "<div class=\"up color\"></div>" + "</td>");
                }
                tableBody.append(row);
            }
        };

        var _updateTopStores = function(topStores) {
            var _topStores = jQuery(".top-stores", matchedObject);
            var bubleContent = jQuery(".bubble-content", _topStores);
            bubleContent.empty();

            var size = topStores.length > 3 ? 3 : topStores.length;

            for (var index = 0; index < size; index++) {
                var item = topStores[index];
                var value = String(item[0]);
                var name = item[1];
                var bubleContents = jQuery("<div class=\"bubble-contents\">"
                        + "<div class=\"value\">" + value + "</div>"
                        + "<div class=\"title\">" + name + "</div>" + "</div>");
                index != 0 && bubleContents.addClass("double");
                bubleContent.append(bubleContents);
            }
        };

        initialize();
        return matchedObject;
    };
})(jQuery);
