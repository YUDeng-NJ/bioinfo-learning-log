import torch, esm, numpy as np
 
model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
model = model.eval().cuda()
bc = alphabet.get_batch_converter()
 
seqs = [('s1', 'MSIQHFRVALIPFFAAFCLPVFAHPETLVKVKDAEDQLGARVGYIELDLNSGKILESFRPEER')]
_, _, tokens = bc(seqs)
tokens = tokens.cuda()
with torch.no_grad():
    out = model(tokens, repr_layers=[33])
vec = out['representations'][33][0, 1:-1].mean(0).cpu().numpy()
np.save('output/week08_embed.npy', vec)
print(vec.shape)
