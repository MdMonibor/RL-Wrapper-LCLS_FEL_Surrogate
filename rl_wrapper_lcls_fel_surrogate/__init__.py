from lume_model.models import TorchModel
from rl_wrapper_lcls_fel_surrogate.const import QUAD_NAMES, buffered_env_ranges, DEFAULTS
from gymnasium.envs.registration import register
from .rl_env import LTUHEnv

model = TorchModel("/Users/monibor/Desktop/HAAI/RL-Wrapper-LCLS_FEL_Surrogate/RL-Wrapper-LCLS_FEL_Surrogate/model_config.yaml")

register(
    id="HAAI_RL01-v0",
    entry_point="rl_wrapper_lcls_fel_surrogate.rl_env:LTUHEnv",
    kwargs={
        "model": model,
        "quad_names": QUAD_NAMES,
        "ranges": buffered_env_ranges,
        "defaults": DEFAULTS,
    },
)
