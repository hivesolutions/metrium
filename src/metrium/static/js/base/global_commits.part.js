(function(jQuery) {
    jQuery.fn.uglobalcommits = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("github.commits_total", function(data) {
                        _updateCommitsTotal(data.commits_total);
                    });
            global.bind("github.commits_data", function(data) {
                        _updateCommitsData(data.commits_data);
                    });
        };

        var _updateCommitsTotal = function(commitsTotal) {
            var _commitsTotal = jQuery(".commits-total", matchedObject);
            var value = jQuery(".value", _commitsTotal);
            var subValue = jQuery(".sub-value", _commitsTotal);
            var progress = jQuery(".progress", _commitsTotal);

            var previous = commitsTotal[0];
            var current = commitsTotal[1];
            var ratio = current / previous;
            ratio = ratio > 1.0 ? 1.0 : ratio;
            ratio *= 100;
            ratio = Math.floor(ratio);
            var ratioS = String(ratio);

            value.text(current);
            subValue.text(previous);

            progress.attr("data-value", ratioS);
            progress.uprogress();
        };

        var _updateCommitsData = function(commitsData) {
            var _commitsData = jQuery(".commits-data", matchedObject);
            var lineChart = jQuery(".line-chart", _commitsData);
            var commitsDataS = String(commitsData);

            lineChart.attr("data-values", commitsDataS);
            lineChart.ulinechart();
        };

        initialize();
        return matchedObject;
    };
})(jQuery);
