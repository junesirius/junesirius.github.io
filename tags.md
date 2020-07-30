---
layout: default
title: 标签
---

<div class="well article">
{% assign sortedtags = site.tags | sort %}
{% for tag in sortedtags %}
    <a id="{{ tag[0] }}" style="position: relative; top: -50px"></a>
    <h2>{{ tag[0] }}</h2>
    <ul>
        {% assign pages_list = tag[1] %}
        {% for node in pages_list %}
            {% if node.title != null %}
            {% if group == null or group == node.group %}
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
            {% endif %}
            {% endif %}
        {% endfor %}
        {% assign pages_list = nil %}
    </ul>
{% endfor %}    
</div>
