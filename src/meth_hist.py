import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

s_8_cell = pd.read_csv('s_8_cell.deduplicated.bismark.cov', sep='\t', 
                       names=['chr', 'start','end', 'meth_percent', 'meth_count', 'unmeth_count'])

epiblast = pd.read_csv('s_epiblast.deduplicated.bismark.cov', sep='\t', 
                       names=['chr', 'start','end', 'meth_percent', 'meth_count', 'unmeth_count'])

icm = pd.read_csv('s_icm.deduplicated.bismark.cov', sep='\t', 
                       names=['chr', 'start','end', 'meth_percent', 'meth_count', 'unmeth_count'])

from google.colab import files

sns.histplot(data=s_8_cell, x='meth_percent', bins=20, kde=True, kde_kws={'bw_adjust': 2})
plt.title("8_cell")
plt.savefig('8_cell_hist.png')
files.download("8_cell_hist.png")

sns.histplot(data=icm, x='meth_percent', bins=20, kde=True, kde_kws={'bw_adjust': 2})
plt.title("icm")
plt.savefig('icm_hist.png')
files.download("icm_hist.png")

sns.histplot(data=epiblast, x="meth_percent", bins=20, kde=True, kde_kws={'bw_adjust': 2})
plt.title("epiblast")
plt.savefig('epiblast_hist.png')
files.download("epiblast_hist.png")