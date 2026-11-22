from sklearn.decomposition import PCA
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
 
X = np.load('output/week08_embed.npy').reshape(1, -1)
pca = PCA(n_components=2)
xy = pca.fit_transform(X)
plt.figure(figsize=(5, 4))
plt.scatter(xy[:, 0], xy[:, 1])
plt.savefig('figs/week08_pca.png', dpi=300)
