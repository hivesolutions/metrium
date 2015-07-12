{% extends "partials/layout_config.html.tpl" %}
{% block title %}GitHub{% endblock %}
{% block name %}Config :: GitHub{% endblock %}
{% block content %}
    {% if config.username %}
        <form action="{{ url_for('do_github_config') }}" method="post" class="form">
            {% if config.username %}
                <div class="label">
                    <label>Username</label>
                </div>
                <div class="input">
                    <input class="text-field" value="{{ config.username }}" data-disabled="1" />
                </div>
                <div class="label">
                    <label>Repos</label>
                </div>
            {% endif %}
            <span class="button" data-link="{{ url_for('base_config') }}">Cancel</span>
            //
            <span class="button" data-submit="true">Update</span>
            <div class="alternative">
            	<span class="button"
            		  data-link="{{ url_for('github_authorize', next = url_for('base_config')) }}">Link Account</span>
            </div>
        </form>
    {% endif %}
{% endblock %}
