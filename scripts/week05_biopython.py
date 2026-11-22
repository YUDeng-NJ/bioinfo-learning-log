from Bio import SeqIO
from Bio import Phylo

print('== 序列统计 ==')
for rec in SeqIO.parse('data/test2.fasta', 'fasta'):
    gc = round((rec.seq.count('G') + rec.seq.count('C')) / len(rec.seq) * 100, 1)
    print(rec.id, len(rec.seq), gc)

print('== 树结构 ==')
tree = Phylo.read('data/test.nwk', 'newick')
print('叶数:', len(tree.get_terminals()))
print('分支数:', len(tree.get_nonterminals()))
for clade in tree.get_nonterminals():
    print(clade.name, [t.name for t in clade.get_terminals()])
