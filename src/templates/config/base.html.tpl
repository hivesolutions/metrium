{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config{% endblock %}
{% block content %}
    <ul>
        <li>
            <div class="name">
                <a href="{{ url_for('mail_config') }}">Mail</a>
            </div>
            <div class="description">IMAP client configuration</div>
        </li>
    </ul>
{% endblock %}
