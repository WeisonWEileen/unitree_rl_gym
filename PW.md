conda activate utgym

python legged_gym/scripts/train.py --task=h1_2 --rl_device=cuda:0 --sim_device=cuda:0

python deploy/deploy_mujoco/deploy_mujoco.py h1_2.yaml

python legged_gym/scripts/play.py --task=h1_2