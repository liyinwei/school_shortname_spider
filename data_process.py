"""
@Author: liyinwei
@E-mail: coridc@foxmail.com
@Time: 2018-12-26 10:15
@Description: TODO
"""

import pandas as pd

df = pd.read_csv('./school_shortname_spider/data/school.csv')

df.dropna(subset=['short_name'], inplace=True)

schools = []
df.apply(
    lambda x: schools.append('%s|%s' % (x['full_name'], x['short_name'].replace('、', '|'))), axis=1
)

pd.DataFrame(schools).to_csv('./school.csv', header=None, index=False)

if __name__ == '__main__':
    pass
