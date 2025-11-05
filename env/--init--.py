from lume_model.models import TorchModel
from const import QUAD_NAMES, buffered_env_ranges, DEFAULTS
from gymnasium.envs.registration import register
model = TorchModel("model_config.yaml")

register(
    id="HAAI_RL01-v0",
    entry_point="haai_env:LTUHEnv",
    kwargs={
        "model": model,
        "quad_names": QUAD_NAMES,
        "env_ranges": buffered_env_ranges,
        "defaults": DEFAULTS,
    },
)