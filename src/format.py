import pandas as pd
import os
os.linesep = '\n' # For fixing double lineterminators in pandas.DataFrame.to_csv(): https://github.com/winpython/winpython/issues/884

# Gemerate Qlik QVS-file

df = pd.read_csv('format.csv',sep=';')
df = df.drop(['num', 'desc'], axis=1)
csv = df.to_csv(sep=';',index=False)
columns = list(df.columns)
columns.remove('char')
mappings = '\n'.join([c+':MAPPING LOAD char, '+c+' RESIDENT FormatTable;' for c in columns])
sets = '\n'.join(['SET '+c+'=MapSubstring('+c+',$1);' for c in columns])

open('../format.qvs','w',encoding='utf-8').write(f"""

FormatTable:
LOAD * INLINE '
{csv}
' (delimiter is ';');

{mappings}

{sets}

DROP TABLE FormatTable;

""")