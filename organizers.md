---
layout: home
title: Organizers
description: Organizers.
image: /images/home/paper_natEcoEvol2020_highres.jpg
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
      {% if person.website %}
        <a href="{{ person.website }}" target="_blank" class="speaker-card-link">
      {% else %}
        <div class="speaker-card-link">
      {% endif %}
        <div class="speaker-img-container">
          <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})"></div>
        </div>
      {% if person.website %}
        </a>
      {% else %}
        </div>
      {% endif %}
      <div class="name">
        {% if person.website %}
          <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
        {% else %}
          {{ person.name }}
        {% endif %}
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
      {% if person.website %}
        <a href="{{ person.website }}" target="_blank" class="speaker-card-link">
      {% else %}
        <div class="speaker-card-link">
      {% endif %}
        <div class="speaker-img-container">
          <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})"></div>
        </div>
      {% if person.website %}
        </a>
      {% else %}
        </div>
      {% endif %}
      <div class="name">
        {% if person.website %}
          <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
        {% else %}
          {{ person.name }}
        {% endif %}
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
      {% if person.website %}
        <a href="{{ person.website }}" target="_blank" class="speaker-card-link">
      {% else %}
        <div class="speaker-card-link">
      {% endif %}
        <div class="speaker-img-container">
          <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})"></div>
        </div>
      {% if person.website %}
        </a>
      {% else %}
        </div>
      {% endif %}
      <div class="name">
        {% if person.website %}
          <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
        {% else %}
          {{ person.name }}
        {% endif %}
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
      {% if person.website %}
        <a href="{{ person.website }}" target="_blank" class="speaker-card-link">
      {% else %}
        <div class="speaker-card-link">
      {% endif %}
        <div class="speaker-img-container">
          <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})"></div>
        </div>
      {% if person.website %}
        </a>
      {% else %}
        </div>
      {% endif %}
      <div class="name">
        {% if person.website %}
          <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
        {% else %}
          {{ person.name }}
        {% endif %}
      </div>
      <div class="position">{{ person.position }}</div>
      <div class="position2">{{ person.position2 }}</div>
      <div class="position3">{{ person.position3 }}</div>
    </li>
  {% endif %}
  {% endfor %}
</ul>
