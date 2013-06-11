{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config :: Mail{% endblock %}
{% block content %}
    <form action="" method="post" class="form">
        <div class="label">
            <label>IMAP Host</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="host" placeholder="eg: imap.host.com" value="{{ config.host }}"
                   data-error="{{ errors.host }}" />
        </div>
        <div class="label">
            <label>Email</label>
        </div>
        <div class="input">
            <input class="text-field" name="email" placeholder="eg: johndoe@host.com" value="{{ config.email }}"
                   data-error="{{ errors.email }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" placeholder="eg: jonhdoepass"
                   value="{{ config.password }}" data-error="{{ errors.password }}" />
        </div>
        <span class="button" data-link="{{ url_for('mail_config') }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
