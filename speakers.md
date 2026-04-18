---
layout: home
title: Invited Speakers
description: Invited speakers
image: /images/home/paper_natEcoEvol2020.jpg
---

<p class="editor-link">
  <a href="cloudcannon:collections/_attendees" class="btn">
    <strong>&#9998;</strong> Manage Staff Members
  </a>
</p>

{% assign grouped_speakers = site.attendees | group_by: "category" %}
{% for group in grouped_speakers %}
  <h2 style="margin-top: 2rem;">{{ group.name }}</h2>
  <ul class="staff">
    {% for person in group.items %}
      <li>
        <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})"></div>
        <div class="name">
          <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
        </div>
        <div class="position">{{ person.position }}</div>
      </li>
    {% endfor %}
  </ul>
{% endfor %}
