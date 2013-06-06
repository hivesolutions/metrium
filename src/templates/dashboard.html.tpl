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
            <div class="context">
                <div class="date">
                    <div class="week-day">Quinta-feira</div>
                    <div class="day">16 Maio</div>
                    <div class="time">14:50</div>
                </div>
                <div class="news-item">
                    <div class="title">
                        <span class="time">16:32</span>
                        <span class="message">John Doe</span>
                        <span class="marker red"></span>
                    </div>
                    <div class="message">
                        Atenção aos prazos de entrega que estão definidos.
                    </div>
                </div>
                <div class="news-item">
                    <div class="title">
                        <span class="time">14:50</span>
                        <span class="message">João Magalhães</span>
                        <span class="marker green"></span>
                    </div>
                    <div class="message">
                        Atenção aos prazos de entrega que estão definidos.
                    </div>
                </div>
            </div>
            <div class="board">
                <div class="line">
                    <div class="box triple"></div>
                </div>
                <div class="line">
                    <div class="box">
                        <div class="box-contents table">
                            <h1>vendas</h1>
                            <h2>lojas</h2>
                            <table>
                                <thead>
                                    <tr>
                                        <th>Loja</th>
                                        <th class="value">ontem</th>
                                        <th class="value">hoje</th>
                                        <th class="marker"></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Dolce Vita</td>
                                        <td class="value">3623,34</td>
                                        <td class="value">36,23</td>
                                        <td class="marker">
                                            <div class="up color"></div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>31 Janeiro</td>
                                        <td class="value">50,23</td>
                                        <td class="value">252,00</td>
                                        <td class="marker">
                                            <div class="up color"></div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>Joia do Tempo</td>
                                        <td class="value">7890,23</td>
                                        <td class="value">2320,42</td>
                                        <td class="marker">
                                            <div class="down color"></div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>Galeria da Jóia</td>
                                        <td class="value">523,22</td>
                                        <td class="value">223,22</td>
                                        <td class="marker">
                                            <div class="up color"></div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="box">
                        <div class="box-contents">
                            <h1>top</h1>
                            <h2>lojas</h2>
                            <div class="bubble-contents">
                                <div class="value">254</div>
                                <div class="title">Galeria da Jóia</div>
                            </div>
                            <div class="bubble-contents double">
                                <div class="value">254</div>
                                <div class="title">Dolce Vita</div>
                            </div>
                            <div class="bubble-contents double">
                                <div class="value">254</div>
                                <div class="title">31 de Janeiro</div>
                            </div>
                        </div>
                    </div>
                    <div class="box">
                        <div class="box-contents">
                            <h1>top</h1>
                            <h2>vendedores</h2>
                            <div class="top-contents">
                                <div class="rank">1</div>
                                <div class="picture">
                                    <img src="/static/images/dummies/dummy_picture_1.png" />
                                </div>
                                <div class="details">
                                    <div class="name">John Doe</div>
                                    <div class="value">362</div>
                                    <div class="amount">1.000,45€</div>
                                </div>
                            </div>
                            <div class="top-contents">
                                <div class="rank">2</div>
                                <div class="picture">
                                    <img src="/static/images/dummies/dummy_picture_2.png" />
                                </div>
                                <div class="details">
                                    <div class="name">Mary Jane</div>
                                    <div class="value">290</div>
                                    <div class="amount">950,00€</div>
                                </div>
                            </div>
                            <div class="top-contents">
                                <div class="rank">3</div>
                                <div class="picture">
                                    <img src="/static/images/dummies/dummy_picture_3.png" />
                                </div>
                                <div class="details">
                                    <div class="name">Christopher Elliot</div>
                                    <div class="value">203</div>
                                    <div class="amount">745,20€</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="status"></div>
                <div class="message"></div>
            </div>
        </div>
    </div>
{% endblock %}
