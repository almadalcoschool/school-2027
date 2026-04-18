---
layout: home
title: Organizers
description: Organizers.
image: /images/home/paper_natEcoEvol2020.jpg
---

<p class="editor-link">
  <a href="cloudcannon:collections/_organizers" class="btn">
    <strong>&#9998;</strong> Manage Staff Members
  </a>
</p>

## Chairpersons
<ul class="staff">
  {% for person in site.organizers %}
  {% if person.role contains "Chairperson" %}
    <li>
      <div class="name">
        <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
      </div>
      <div class="position">{{ person.position }}</div>
      <div class="position2">{{ person.position2 }}</div>
      <div class="position3">{{ person.position3 }}</div>
    </li>
  {% endif %}
  {% endfor %}
</ul>

## Scientific Committee of the School
<ul class="staff">
  {% for person in site.organizers %}
  {% if person.role contains "Scientific Committee" %}
    <li>
      <div class="name">
        <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
      </div>
      <div class="position">{{ person.position }}</div>
      <div class="position2">{{ person.position2 }}</div>
      <div class="position3">{{ person.position3 }}</div>
    </li>
  {% endif %}
  {% endfor %}
</ul>

## Local Organizing Committee
<ul class="staff">
  {% for person in site.organizers %}
  {% if person.role contains "Local Organizing Committee" %}
    <li>
      <div class="name">
        <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
      </div>
      <div class="position">{{ person.position }}</div>
      <div class="position2">{{ person.position2 }}</div>
      <div class="position3">{{ person.position3 }}</div>
    </li>
  {% endif %}
  {% endfor %}
</ul>

## Webmasters
<ul class="staff">
  {% for person in site.organizers %}
  {% if person.role contains "Webmasters" %}
    <li>
      <div class="name">
        <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
      </div>
      <div class="position">{{ person.position }}</div>
      <div class="position2">{{ person.position2 }}</div>
      <div class="position3">{{ person.position3 }}</div>
    </li>
  {% endif %}
  {% endfor %}
</ul>
