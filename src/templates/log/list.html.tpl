{% extends "partials/layout_log_l.html.tpl" %}
{% block title %}Log{% endblock %}
{% block name %}Log{% endblock %}
{% block content %}
    <ul class="filter" data-no_input="1">
        <div class="data-source" data-url="{{ url_for('list_logs_json') }}" data-type="json" data-timeout="0"></div>
        <li class="template table-row">
            <div class="status text-left" data-width="420">%[message]</div>
            <div class="date text-left" data-width="160">%[type]</div>
            <div class="table-clear"></div>
        </li>
        <div class="filter-no-results quote">
            No results found
        </div>
        <div class="filter-more">
            <span class="button more">Load more</span>
            <span class="button load">Loading</span>
        </div>
    </ul>
{% endblock %}
