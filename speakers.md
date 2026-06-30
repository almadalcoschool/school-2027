---
layout: home
title: Invited Speakers
description: Invited speakers
image: /images/home/paper_natEcoEvol2020.jpg
---

<style>
.staff li {
  padding: 30px 10px;
}
.speaker-img-container {
  display: block;
  position: relative;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto;
  box-shadow: 0 4px 15px rgba(0,0,0,0.15);
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.speaker-img-container:hover {
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

.bio-hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(43, 43, 64, 0.94);
  color: #ffffff;
  opacity: 0;
  transition: opacity 0.35s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 18px;
  border-radius: 50%;
  box-sizing: border-box;
}

.speaker-img-container:hover .bio-hover-overlay {
  opacity: 1;
}

.bio-text {
  font-size: 0.72rem;
  line-height: 1.4;
  margin: 0;
  text-align: center;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 8;
  -webkit-box-orient: vertical;
  color: #f5f5fa;
  font-family: inherit;
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
        <div class="speaker-img-container">
          <a href="{{ person.website }}" target="_blank">
            <div class="square-image" style="background-image: url({% include relative-src.html src=person.image_path %})">
              {% if person.bio %}
                <div class="bio-hover-overlay">
                  <span class="bio-text">{{ person.bio }}</span>
                </div>
              {% endif %}
            </div>
          </a>
        </div>
        <div class="name">
          <a href="{{ person.website }}" target="_blank">{{ person.name }}</a>
        </div>
        <div class="position">{{ person.position }}</div>
      </li>
    {% endfor %}
  </ul>
{% endfor %}
