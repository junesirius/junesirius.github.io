---
layout: default
title: 长篇
---
<!-- Look for the name list of all long-novels -->
{% assign long_novel_posts = site.posts | where_exp:"post", "post.long_novels != null" %}
{% assign long_novel_list = "" | split: "" %}

{% for post in long_novel_posts %}
    {% unless long_novel_list contains post.long_novels %}
        {% assign long_novel_list = long_novel_list | push: post.long_novels %}
    {% endunless %}
{% endfor %}

<!-- Begin display-->
<div class="well article">
{% assign sortedlongnovels = long_novel_list | sort %}
{% for longnovel in sortedlongnovels %}
    <a id="{{ longnovel }}" style="position: relative; top: -50px"></a>
    <h2>{{ longnovel }}</h2>
    <ul>
        {% for node in site.posts %}
            {% if node.title != null and node.long_novels == longnovel %}
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
        {% endfor %}
    </ul>
{% endfor %}    
</div>
