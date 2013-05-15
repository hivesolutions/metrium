{% include "partials/doctype.html.tpl" %}
<head>
    {% block head %}
        {% include "partials/content_type.html.tpl" %}
        {% include "partials/includes.html.tpl" %}
        <title>Metrium / {% block title %}{% endblock %}</title>
    {% endblock %}
</head>
<body class="ux fullscreen wait-load">
    <div id="overlay" class="overlay"></div>
    <div id="content">{% block content %}{% endblock %}</div>
</body>
{% include "partials/end_doctype.html.tpl" %}
