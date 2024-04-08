---
title: Major Calendars
permalink: /schedules/major/
toc: false
---

{% assign schedule_files = site.static_files | where: "division", "major" %}
{% for sched_file in schedule_files %}
* [{{ sched_file.name }}]({{ sched_file.path }})
{% endfor %}
