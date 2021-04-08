#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import numpy as np
# from functools import partial


# pilgrim
# pilgrims_Camino_Santiago_2004-2019.csv
# https://raw.githubusercontent.com/luisballesteros/caminodesantiago/main/pilgrims_Camino_Santiago_2004-2019.csv
pilgrim = "pilgrims_Camino_Santiago_2004-2019.csv"
pilgrim_df = pd.read_csv(pilgrim)
pilgrim_df = pilgrim_df.set_index("year")
# calculate % by gender
pilgrim_percent_df = pilgrim_df.div(pilgrim_df.sum(axis=1), axis=0)*100
print(pilgrim_percent_df)

# athletics
# https://raw.githubusercontent.com/luisballesteros/caminodesantiago/main/athletics_licenses_by_gender.csv
athletics = "athletics_licenses_by_gender.csv"
athletics_df = pd.read_csv(athletics)
athletics_df .drop(columns=['total'], inplace=True)
athletics_df = athletics_df.set_index("year")
# athletics_df .apply(partial(pd.to_numeric, errors='ignore')).info()
# calculate % by gender
athletics_percent_df = athletics_df.div(athletics_df.sum(axis=1), axis=0)*100
print(athletics_percent_df)

# Graphical representation
# 2 graphs distributed vertically and share x and y axis.
# Size with golden ratio.
fig, (ax1, ax2) = plt.subplots(2, sharey=True, sharex=True, figsize=(10, 16))
pilgrim_percent_df.plot(ax=ax1, legend=False)
# despine removes frames and with true left also removes the left one.
sns.despine(left=True)
sns.set_style("white")
sns.set_style("ticks")
plt.xlabel('year')
ax1.yaxis.set_label_text('% male/female')
ax1.set_title('% pilgrim "Camino de Santiago" by gender Yearly')
athletics_percent_df.plot(ax=ax2)
ax2.yaxis.set_label_text('% male/female')
plt.legend(frameon=False, loc='lower left')
ax2.set_title('% of athletic licenses by gender Yearly')
plt.savefig('pilgrimbygender.png')
plt.show()
