---
layout: default
title: 归档
---

<div class="well article">
{%for post in site.posts %}
    {% unless post.next %}
        <h2>{{ post.date | date: '%Y' }}</h2>
        <ul>
    {% else %}
        {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
        {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
        {% if year != nyear %}
            </ul>
            <h2>{{ post.date | date: '%Y' }}</h2>
            <ul>
        {% endif %}
    {% endunless %}
    <li>
        <span class="post-date">
            {% assign date_format = site.date_format.archive %}
            {{ post.date | date: date_format }}
        </span>
        {% if post.title contains "梦记" or post.tags contains "梦记" or post.tags contains "观后感" or post.categories contains "观后感" %}
            <span class="a-light"><a href="{{ site.baseurl}}{{ post.url }}">{{ post.title }}</a></span>
        {% else %}
            <a href="{{ site.baseurl}}{{ post.url }}">{{ post.title }}</a>
        {% endif %}
    </li>
{% endfor %}
</ul>
</div>
