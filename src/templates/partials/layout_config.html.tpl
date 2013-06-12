{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("config.base") %}
            {% if sub_link == "base" %}
                <a href="{{ url_for('base_config') }}" class="active">base</a>
            {% else %}
                <a href="{{ url_for('base_config') }}">base</a>
            {% endif %}
        {% endif %}
        {% if acl("config.mail") %}
            //
            {% if sub_link == "mail" %}
                <a href="{{ url_for('mail_config') }}" class="active">mail</a>
            {% else %}
                <a href="{{ url_for('mail_config') }}">mail</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}