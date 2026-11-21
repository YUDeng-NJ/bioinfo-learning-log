import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
 
df = pd.read_csv('data/BLAT_ECOLX_Deng_2012.csv')
parts = df['mutant'].str.extract(r'^([A-Z])(\d+)([A-Z])$')
df['pos'] = parts[1].astype(int)
 
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(df['DMS_score'], bins=40, color='#4A90D9')
ax.set_xlabel('DMS score')
ax.set_ylabel('count')
ax.set_title('Distribution of fitness scores')
fig.tight_layout()
fig.savefig('figs/week04_hist.png', dpi=300)
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(df['pos'], df['DMS_score'], s=6, alpha=0.4, color='#4A90D9')
ax.axhline(0, color='grey', linewidth=1, linestyle='--')
ax.set_xlabel('residue position')
ax.set_ylabel('DMS score')
ax.set_title('Fitness by position')
fig.tight_layout()
fig.savefig('figs/week04_scatter.png', dpi=300)
