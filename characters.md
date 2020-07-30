---
layout: default
title: 人物
---
<!-- Look for the name list of all characters -->
{% assign character_list = "" | split: "" %}
{% for node in site.posts %}
    {% for character in node.characters %}
        {% unless character_list contains character %}
            {% assign character_list = character_list | push: character %}
        {% endunless %}
    {% endfor %}
{% endfor %}

<!-- Begin display-->
<div class="well article">
{% assign sortedcharacters = character_list | sort %}
{% for character in sortedcharacters %}
    <a id="{{ character }}" style="position: relative; top: -50px"></a>
    <h2>{{ character }}</h2>
    <ul>
        {% for node in site.posts %}
            {% for post_character in node.characters %}
                {% if post_character == character and node.title != null%}
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
                    {% break %}
                {% endif %}
            {% endfor %}
        {% endfor %}
    </ul>
{% endfor %}    
</div>
