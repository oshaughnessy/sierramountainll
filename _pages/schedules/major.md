---
title: Major Calendars
permalink: /schedules/major/
toc: false
league: baseball
division: Major
---

{% include_relative schedule.html league=page.league division=page.division %}

{% assign schedule_files = site.static_files | where: "division", "major" %}
{% for sched_file in schedule_files %}
* [{{ sched_file.name }}]({{ sched_file.path }})
{% endfor %}

## Angels
<iframe src="https://calendar.google.com/calendar/embed?src=k2ur6vqrl6hv2f8l3pun3ko9q8ejro9g%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Braves
<iframe src="https://calendar.google.com/calendar/embed?src=krjqful4pi3p5tmpgo72qfjvemkq0agj%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Dodgers
<iframe src="https://calendar.google.com/calendar/embed?src=27i5s9mh2mkn90be2vq4vgr4n3emctt1%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
