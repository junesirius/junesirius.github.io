---
layout: default
title: 分类
---

<div class="well article">
{% assign sortedcategories = site.categories | sort %}
{% for category in sortedcategories %}
    <a id="{{ category[0] }}" style="position: relative; top: -50px"></a>
    <h2><a href="{{ site.baseurl }}/categories-detail#{{ category[0] }}">{{ category[0] }}</a></h2>
    <ul>
    {% assign pages_list = category[1] %}
    <!-- Find tags and characters under the category -->
    {% assign ctg_tag_list = "" | split: "" %}
    {% assign ctg_character_list = "" | split: "" %}
    {% for node in pages_list %}
        {% for tag in node.tags %}
            {% unless ctg_tag_list contains tag %}
                {% assign ctg_tag_list = ctg_tag_list | push: tag %}
            {% endunless %}
        {% endfor %}
        {% for character in node.characters %}
            {% unless ctg_character_list contains character %}
                {% assign ctg_character_list = ctg_character_list | push: character %}
            {% endunless %}
        {% endfor %}
    {% endfor %}
    {% assign pages_list = nil %}
    <!-- Display tags under the category -->
    {% if ctg_tag_list.size > 0 %}
    <li>
        <span><strong>标签：</strong></span>
        {% assign ctg_tag_list = ctg_tag_list | sort %}
            {% for tag in ctg_tag_list %}
                <span>
                    <a href="{{ site.baseurl }}/tags#{{ tag }}">{{ tag }}</a>
                </span>
                {% unless forloop.last %}
                &nbsp;|&nbsp; 
                {% endunless %}
            {% endfor %}
    </li>
    {% endif %}
    {% assign ctg_tag_list = nil %}
    <!-- Display characters under the category -->
    {% if ctg_character_list.size > 0 %}
    <li>
        <span><strong>人物：</strong></span>
        {% assign ctg_character_list = ctg_character_list | sort %}
            {% for character in ctg_character_list %}
                <span>
                    <a href="{{ site.baseurl }}/characters#{{ character }}">{{ character }}</a>
                </span>
                {% unless forloop.last %}
                &nbsp;|&nbsp; 
                {% endunless %}
            {% endfor %}
    </li>
    {% endif %}
    {% assign ctg_character_list = nil %}
    </ul>
{% endfor %}
</div>
