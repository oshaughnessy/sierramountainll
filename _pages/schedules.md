---
title: Schedules
permalink: /schedules/
toc: false
---

## 2024 Game Schedules

{% assign schedule_files = site.static_files | where: "schedule", true %}
{% for sched_file in schedule_files %}
* [{{ sched_file.name }}]({{ sched_file.path }})
{% endfor %}
