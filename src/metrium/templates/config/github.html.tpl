{% extends "partials/layout_config.html.tpl" %}
{% block title %}GitHub{% endblock %}
{% block name %}Config :: GitHub{% endblock %}
{% block content %}
    <form action="{{ url_for('do_github_config') }}" method="post" class="form">
        <span class="button" data-link="{{ url_for('github_authorize') }}">Link Account</span>
    </form>
{% endblock %}
