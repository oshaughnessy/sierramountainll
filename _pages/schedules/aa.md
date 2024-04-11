---
title: Player Pitch Calendars
permalink: /schedules/aa/
toc: false
---

{% assign schedule_files = site.static_files | where: "division", "aa" %}
{% for sched_file in schedule_files %}
* [{{ sched_file.name }}]({{ sched_file.path }})
{% endfor %}

## Mets AA[^stale]
<iframe src="https://calendar.google.com/calendar/embed?src=l2rnsf35sg8horuji8npfn5jpnsi2a9m%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Orioles AA[^stale]
<iframe src="https://calendar.google.com/calendar/embed?src=auiha400doqffcfq9eg15jmu0ojkblcv%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Rangers AA[^stale]
<iframe src="https://calendar.google.com/calendar/embed?src=lm5t3p8jtes6uheg8okmpsa3qnunma8c%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

[^stale]: Please note that the most current schedule information is only
          available in [GameChanger](https://web.gc.com). All schedules here may
          be a day or more out of date.
