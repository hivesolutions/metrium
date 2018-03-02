{% set logo_url = config.conf("METRIUM_LOGO_URL") %}
<div class="error-panel">
    <div class="logo" style="{% if logo_url %}background-image: url({{ logo_url }});{% endif %}"></div>
    <h1>Oops!</h1>
    <h2>There seems to be a problem with metrium</h2>
</div>
