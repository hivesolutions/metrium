{% extends "partials/layout_config.html.tpl" %}
{% block title %}GitHub{% endblock %}
{% block name %}Config :: GitHub{% endblock %}
{% block content %}
    <form class="form">
        {% if config.username %}
            <div class="label">
                <label>Username</label>
            </div>
            <div class="input">
                <input class="text-field" name="username" value="{{ config.username }}"
                       data-disabled="1" />
            </div>
        {% endif %}
        <span class="button" data-link="{{ url_for('base_config') }}">Cancel</span>
        //
        <span class="button" data-link="{{ url_for('github_authorize', next = url_for('base_config')) }}">Link Account</span>
    </form>
{% endblock %}
