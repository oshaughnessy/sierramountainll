---
title: League Age &amp; Divisions
tag: signup
toc: true
---

{% assign cur_year = 'now' | date: '%Y' %}
{% assign last_year = cur_year | minus: 1 %}

{% assign bb_4y = cur_year | minus: 4 %}
{% assign bb_5y = cur_year | minus: 5 %}
{% assign bb_6y = cur_year | minus: 6 %}
{% assign bb_7y = cur_year | minus: 7 %}
{% assign bb_8y = cur_year | minus: 8 %}
{% assign bb_9y = cur_year | minus: 9 %}
{% assign bb_10y = cur_year | minus: 10 %}
{% assign bb_11y = cur_year | minus: 11 %}
{% assign bb_12y = cur_year | minus: 12 %}
{% assign bb_13y = cur_year | minus: 13 %}
{% assign bb_14y = cur_year | minus: 14 %}
{% assign bb_22y = cur_year | minus: 22 %}

{% assign sb_4y = last_year | minus: 4 %}
{% assign sb_5y = last_year | minus: 5 %}
{% assign sb_6y = last_year | minus: 6 %}
{% assign sb_7y = last_year | minus: 7 %}
{% assign sb_8y = last_year | minus: 8 %}
{% assign sb_9y = last_year | minus: 9 %}
{% assign sb_10y = last_year | minus: 10 %}
{% assign sb_11y = last_year | minus: 11 %}
{% assign sb_12y = last_year | minus: 12 %}
{% assign sb_13y = last_year | minus: 13 %}
{% assign sb_14y = last_year | minus: 14 %}

How does your player's age affect the division they'll be in?
It's a key way to identify the starting point for players in
the league.

It's not always the only factor, though -- you can see that
there's some overlap in the groups below.  Players who want
to play in AAA and above will need to attend an assessment.
One or more are offered before every season begins.

SMLL has established the following age groups:

## <span class="baseball">Baseball</span>
{: .baseball }

A player's "league age" for baseball is the age they will be by the end of August 31
in the current season's year.

| Division           -| League Age Range  
|---------------------|-------------------
| Tee Ball            | 6-4 years old     
| Minor Coach Pitch   | 6-5 years old     
| Minor Player Pitch  | 9-7 years old     
| Minor AAA           | 10-8 years old    
| Major               | 12-10 years old   
| 50/70               | 13-11 years old   

## <span class="softball">Softball</span>
{: .softball}

A player's "league age" for softball is the age they were at the end of the 
year preceding the season. In other words, how old were they last Dec 31?

In the first year of SMLL softball, 2023, we used age-based divisions
to align with nearby fastpitch youth leagues that use softball's
more conventional 2-year groupings. We're considering expanding each
division in 2024 to create larger Minor and Major divisions and
facilitate a strong Junior team.

### 2024+

| Division                -| League Age Range | Birth Years
|--------------------------|------------------|------------
| 6U (Minor Coach Pitch)   | 6-5              | {{sb_6y}}-{{sb_5y}}
| 9U (Minor Player Pitch)  | 9-7              | {{sb_9y}}-{{sb_7y}}
| 12U (Major)              | 12-10            | {{sb_12y}}-{{sb_10y}} [^SBT]
| 14U (Junior)             | 14-12            | {{sb_14y}}-{{sb_12y}} [^SBT]

[^SBT]: aligns with the age range for a Little League softball tournament division

### 2023

| Division                  -| League Age Range
|----------------------------|-----------------
| 6U (Coach Pitch)           | 6-5
| 8U (Coach & Player Pitch)  | 8-7
| 10U                        | 10-9
| 12U (Major)                | 12-11

## <span class="challenger">Challenger</span>
{: .challenger}

A player's "league age" for Challenger baseball is the age they will be by the end
of August 31 in the current season's year.

| Division                 -| Age Range                     | Birth Months
|---------------------------|-------------------------------|-
| Challenger                | 4-18 (22 if still in school)  | 9/{{bb_22y}}-8/{{bb_4y}}
| [Senior](https://www.littleleague.org/play-little-league/challenger/senior-division/) | 15+ [^SC]

[^SC]: SMLL does not offer a Senior Challenger division.

## League Age

We use the league age to fit players into the categories above. Note that the
formula for baseball and softball is different.

See the [Little League age calculator](https://www.littleleague.org/play-little-league/determine-league-age/){:target="_blank"}
for more information.

Please Note: Only players age 8 and above must attend a player assessment
{: .notice}
