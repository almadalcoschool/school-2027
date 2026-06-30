---
layout: home
title: Invited Speakers
description: Invited speakers
image: /images/home/paper_natEcoEvol2020_highres.jpg
---

<style>
.staff li {
  padding: 30px 10px;
  position: relative;
}
.speaker-card-link {
  display: block;
  position: relative;
  text-decoration: none;
  margin: 0 auto;
  width: 200px;
  height: 200px;
}
.speaker-img-container {
  display: block;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.15);
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.speaker-card-link:hover .speaker-img-container {
  transform: translateY(-6px);
  box-shadow: 0 12px 28px rgba(0,0,0,0.22);
}

.speaker-img-container .square-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  margin: 0;
  position: relative;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

.bio-tooltip-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0.9);
  width: 270px;
  background: rgba(30, 30, 46, 0.98);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #f5f5fa;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), visibility 0.3s;
  z-index: 100;
  pointer-events: none;
  box-sizing: border-box;
}

.speaker-card-link:hover .bio-tooltip-box {
  opacity: 1;
  visibility: visible;
  transform: translate(-50%, -50%) scale(1);
}

.bio-text {
  font-size: 0.74rem;
  line-height: 1.45;
  margin: 0;
  text-align: left;
  color: #e2e2e9;
  display: block;
  font-family: 'Rubik', 'Lato', sans-serif;
  font-weight: 300;
}
</style>

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
        <a href="{{ person.website }}" target="_blank" class="speaker-card-link">
          <div class="speaker-img-container">
            <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})"></div>
          </div>
          {% if person.bio %}
            <div class="bio-tooltip-box">
              <span class="bio-text">{{ person.bio }}</span>
            </div>
          {% endif %}
        </a>
        <div class="name">
          <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
        </div>
        <div class="position">{{ person.position }}</div>
      </li>
    {% endfor %}
  </ul>
{% endfor %}
