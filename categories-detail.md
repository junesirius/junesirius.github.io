---
layout: default
title: 标签
---

<div class="well article">
{% assign sortedcategories = site.categories | sort %}
{% for category in sortedcategories %}
    <a id="{{ category[0] }}" style="position: relative; top: -50px"></a>
    <h2><a href="{{ site.baseurl }}/categories#{{ category[0] }}">{{ category[0] }}</a></h2>
    <ul>
        {% assign pages_list = category[1] %}
        {% for node in pages_list %}
            {% if node.title != null %}
            {% if group == null or group == node.group %}
                <div class="row" style="margin: 0; padding: 0">
                <li>
                    <div class="col-md-10" style="margin: 0; padding: 0">
                        <a href="{{ site.baseurl}}{{ node.url }}"> {{ node.title }}</a>
                    </div>
                    <div class="col-md-2" style="margin: 0; padding: 0">
                        <span class="post-date">
                        {% assign date_format = site.date_format.tags %}
                        {{ node.date | date: date_format }}
                        </span>
                    </div>
                </li>
                </div>
            {% endif %}
            {% endif %}
        {% endfor %}
        {% assign pages_list = nil %}
    </ul>
{% endfor %}
</div>
