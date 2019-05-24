# Project 1: SAT & ACT Analysis - Executive Summary

## Problem Statement

What can be learned from ACT & SAT 2017/2018 data, and how can we gain insights to improve SAT Participation rates?

## Executive Summary

In this project, we documented the process of obtaining text-based data, cleaning via Pandas, and plotting data to extract insights.

By utilizing Seasborn/Matplotlib visualization, data is displayed in queries, histograms, boxplots and scatterplots.

## Process:

- [2017/2018 Data Import & Cleaning]
- [Exploratory Data Analysis]
- [Data Visualization]
- [Descriptive and Inferential Statistics]
- [Outside Research]
- [Conclusions and Recommendations]

## Data Dictionary

|Serial Number|Feature|Type|Dataset|Description|
|---|---|---|---|---|
|1|**state**|*Object*|ACT/SAT|State name of United States|
|2|**participation_a17**|*float*|ACT|Participation rate 2017 *(%)*|
|3|**englist_a17**|*float*|ACT|English Score 2017|
|4|**math_a17**|*float*|ACT|Math Score 2017|
|5|**science_a17**|*float*|ACT|Science Score 2017|
|6|**composite_a17**|*float*|ACT|Composite Score 2017|
|7|**participation_a18**|*float*|ACT|Participation rate 2018*(%)* |
|8|**englist_a18**|*float*|ACT|English Score 2018|
|9|**math_a18**|*float*|ACT|Math Score 2018|
|10|**science_a18**|*float*|ACT|Science Score 2018|
|11|**composite_a18**|*float*|ACT|Composite Score 2018|
|12|**participation_s17**|*float*|SAT|Participation rate 2017*(%)* |
|13|**reading_s17**|*int*|SAT| Evidence-Based Reading and Writing Score 2017|
|14|**maths_s17**|*int*|SAT| Math Score 2018|
|15|**total_s17**|*int*|SAT| Total Score 2018|
|12|**participation_s18**|*float*|SAT|Participation rate 2018*(%)* |
|13|**reading_s18**|*int*|SAT| Evidence-Based Reading and Writing Score 2018|
|14|**maths_s18**|*int*|SAT| Math Score 2018|
|15|**total_s18**|*int*|SAT| Total Score 2018|
|16|**dfact2017**|*dataframe*|ACT|ACT 2017 Dataframe|
|17|**dfact2018**|*dataframe*|ACT|ACT 2018 Dataframe|
|18|**dfsat2017**|*dataframe*|SAT|SAT 2017 Dataframe|
|19|**dfsat2018**|*dataframe*|SAT|SAT 2018 Dataframe|
|20|**combined17**|*dataframe*|SAT & ACT|Combined 2017 SAT & ACT Dataframe|
|21|**combined18**|*dataframe*|SAT & ACT|Combined 2018 SAT & ACT Dataframe|
|22|**final**|*dataframe*|SAT & ACT|Combined 2017/2018 SAT & ACT Dataframe|


## Conclusions and Recommendations

### Conclusions:  

While reviewing ACT and SAT participation data from 2017 and 2018, as well state laws regarding testing requirements, we recommend that the College Board prioritize its marketing and lobbying efforts in New Mexico. New Mexico saw an increase from 11% SAT participation in 2017 to 16% in 2018 and still leaves a major room for growth. This contrasts with an ACT participation rate that had a slight increase from 66% to 67%. A slow down in growth in ACT might be due to the neighbouring state, Colorado's transition from ACT to SAT.

### Recommendations:

1) Invest in marketing efforts

New Mexico is a state where students have the freedom to choose the college exam they prefer, or to skip it altogether. With this, there is a contingent of potential customers still untapped by the ACT exam that may be reached by effective communication.

2) Leveraing on past successes

Lobbying and marketing efforts should make use of trends in Texas and Colorado, where SAT participation rates are on a upward trend . This momentum can be harnessed to increase SAT participation rates across the region.

## Data Sources
https://blog.prepscholar.com/act-vs-sat
https://www.usnews.com/education/best-colleges/articles/2018-01-23/how-to-take-the-sat-act-for-free
https://blog.prepscholar.com/which-states-require-the-sat
https://www.edweek.org/ew/section/multimedia/states-require-students-take-sat-or-act.html