{% extends "partials/layout_full.html.tpl" %}
{% block title %}Dashboard{% endblock %}
{% block name %}Dashboard{% endblock %}
{% block content %}
    <div class="dashboard">
        <div class="pusher" data-key="73ce330c0a4efe4266a2"></div>
        <div class="header">
            <div class="logo"></div>
            <ul class="sections">
                <li class="active">home</li>
                <li>arranjos</li>
                <li>encomendas</li>
                <li>vendas</li>
                <li>gravações</li>
            </ul>
        </div>
        <div class="frame">
            <div class="context"></div>
            <div class="board">
                <div class="line">
                    <div class="box"></div>
                    <div class="box double"></div>
                </div>
                <div class="line">
                    <div class="box triple"></div>
                </div>

                <div class="status"></div>
                <div class="message"></div>
            </div>
        </div>
    </div>
{% endblock %}
