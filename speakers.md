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

<ul class="staff">
  {% for person in site.attendees %}
    <li>
      <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})"></div>
      <div class="name">
        <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
      </div>
      <div class="position">{{ person.position }}</div>
      <div class="position2">{{ person.position2 }}</div>
      <div class="position3">{{ person.position3 }}</div>
    </li>
  {% endfor %}
</ul>
