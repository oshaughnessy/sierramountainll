---
title: Major Calendars
permalink: /schedules/major/
toc: false
---

{% assign schedule_files = site.static_files | where: "division", "major" %}
{% for sched_file in schedule_files %}
* [{{ sched_file.name }}]({{ sched_file.path }})
{% endfor %}

## Angels[^stale]
<iframe src="https://calendar.google.com/calendar/embed?src=k2ur6vqrl6hv2f8l3pun3ko9q8ejro9g%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Braves[^stale]
<iframe src="https://calendar.google.com/calendar/embed?src=krjqful4pi3p5tmpgo72qfjvemkq0agj%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Dodgers[^stale]
<iframe src="https://calendar.google.com/calendar/embed?src=27i5s9mh2mkn90be2vq4vgr4n3emctt1%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

[^stale]: Please note that the most current schedule information is only
          available in [GameChanger](https://web.gc.com). All schedules here may
          be a day or more out of date.
