{% extends "partials/layout_account.html.tpl" %}
{% block title %}Accounts{% endblock %}
{% block name %}Accounts :: {{ account.username }}{% endblock %}
{% block content %}
    <form action="{{ url_for('update_account', username = account.username) }}" method="post" class="form">
        <div class="label">
            <label>Username</label>
        </div>
        <div class="input">
            <input class="text-field" name="username" placeholder="eg: johndoe" value="{{ account.username }}"
                   data-disabled="1" data-error="{{ errors.username }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" placeholder="eg: jonhdoepass"
                   value="{{ account.password }}" data-error="{{ errors.password }}" />
        </div>
        <div class="label">
            <label>Confirm Password</label>
        </div>
        <div class="input">
            <input  type="password" class="text-field" name="password_confirm" placeholder="eg: jonhdoepass"
                    value="{{ account.password_confirm }}" data-error="{{ errors.password_confirm }}" />
        </div>
        <div class="label">
            <label>Email</label>
        </div>
        <div class="input">
            <input class="text-field" name="email" placeholder="eg: johndoe@example.com" value="{{ account.email }}"
                   data-error="{{ errors.email }}" />
        </div>
        <span class="button" data-link="{{ url_for('show_account', username = account.username) }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
