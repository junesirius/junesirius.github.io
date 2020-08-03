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
    <!-- Look for the name list of all characters -->
    {% assign character_list = "" | split: "" %}
    {% for node in site.posts %}
        {% for character in node.characters %}
            {% unless character_list contains character %}
                {% assign character_list = character_list | push: character %}
            {% endunless %}
        {% endfor %}
    {% endfor %}
    {% assign character_list = character_list | sort %}
    {% assign character_num = character_list | size %}
    <!-- Look for the count for each character -->
    {% assign character_count_list = "" | split: "" %}
    {% for character in character_list %}
        {% assign character_count = 0 %}
        {% for node in site.posts %}
            {% for node_character in node.characters %}
                {% if node_character == character %}
                    {% assign character_count = character_count | plus: 1 %}
                    {% break %}
                {% endif %}
            {% endfor %}
        {% endfor %}
        {% assign character_count_list = character_count_list | push: character_count %}
        {% assign character_count = 0 %}
    {% endfor %}
    <!-- Look for the max character count -->
    {% assign sorted_character_count = character_count_list | sort | reverse %}
    {% assign max_character_count = sorted_character_count[0] %}
    <!-- Begin display -->
    {% assign character_num_minus = character_num | minus: 1 %}
    {% for character_count_index in (1..max_character_count) reversed %}
        {% for i in (0..character_num_minus) %}
            {% if character_count_list[i] == character_count_index %}
                <a href="{{ site.baseurl }}/characters.html#{{ character_list[i] }}">{{ character_list[i] }} ({{ character_count_list[i] }})</a>
                &nbsp;|&nbsp;
            {% endif %}
        {% endfor %}
    {% endfor %}
    <span><b>人物总数：{{ character_num }}</b></span>
</div>

<div class="well article">
    <h2>长篇</h2>
</div>

<div class="well article">
    <h2>日期</h2>
</div>