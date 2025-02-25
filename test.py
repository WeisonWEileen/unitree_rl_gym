import torch

model1 = torch.jit.load('/home/harlab/tzx/legged_gym-master/logs/centaur_terrain/Jan06_21-26-04_/traced/Jan06_21-26-04__actorbackbone_jit_20000.pt')
print("success1")

model2 = torch.jit.load('/home/harlab/tzx/legged_gym-master/logs/centaur_terrain/Jan06_21-26-04_/traced/Jan06_21-26-04__hist_encoder_jit_20000.pt')
print("success2")