---
layout: default
title: 统计
---
<div class="well article">
    <h2>圈子</h2>
    <!-- Find the max category count -->
    {% assign sorted_categories = site.categories | sort %}
    {% assign max_category_count = 0 %}
    {% for category in sorted_categories %}
        {% if category[1].size > max_category_count %}
            {% assign max_category_count = category[1].size %}
        {% endif %}
    {% endfor %}
    <!-- Begin display -->
    {% for i in (1..max_category_count) reversed %}
        {% for category in sorted_categories %}
            {% if category[1].size == i %}
                <a href="{{ site.baseurl }}/categories.html#{{ category[0] }}">{{ category[0] }} ({{ category[1].size }})</a>
                &nbsp;|&nbsp;
            {% endif %}
        {% endfor %}
    {% endfor %}
    <span><b>圈子个数：{{ site.categories | size }}</b></span>
</div>

<div class="well article">
    <h2>标签</h2>
    <!-- Find the max tag count -->
    {% assign sorted_tags = site.tags | sort %}
    {% assign max_tag_count = 0 %}
    {% for tag in sorted_tags %}
        {% if tag[1].size > max_tag_count %}
            {% assign max_tag_count = tag[1].size %}
        {% endif %}
    {% endfor %}
    <!-- Begin display -->
    {% for i in (1..max_tag_count) reversed %}
        {% for tag in sorted_tags %}
            {% if tag[1].size == i %}
                <a href="{{ site.baseurl }}/tags.html#{{ tag[0] }}">{{ tag[0] }} ({{ tag[1].size }})</a>
                &nbsp;|&nbsp;
            {% endif %}
        {% endfor %}
    {% endfor %}
    <span><b>标签个数：{{ site.tags | size }}</b></span>
</div>

<div class="well article">
    <h2>人物</h2>
</div>

<div class="well article">
    <h2>长篇</h2>
</div>

<div class="well article">
    <h2>日期</h2>
</div>