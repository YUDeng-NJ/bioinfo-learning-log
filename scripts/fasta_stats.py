import argparse, glob, os

from tqdm import tqdm
 
def main():
    ap = argparse.ArgumentParser(description='统计目录下所有 fasta 的条数与总长')
    ap.add_argument('--indir', required=True, help='存放 fasta 的目录')
    ap.add_argument('--out', default='output/stats.csv', help='结果输出路径')
    args = ap.parse_args()
    if not os.path.isdir(args.indir):
        print('目录不存在:', args.indir)
        raise SystemExit(1)

    rows = []
    for path in tqdm(sorted(glob.glob(os.path.join(args.indir, '*.fasta')))):
        n = 0
        with open(path, encoding='utf-8') as f:
            for line in f:
                if line.startswith('>'):
                    n += 1
        rows.append((os.path.basename(path), n))
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write('file,n_seqs\n')
        for name, n in rows:
            f.write(name + ',' + str(n) + '\n')
    print('处理文件数:', len(rows))
 
if __name__ == '__main__':
    main()
