from .lora import *
from .dataset import *
from .utils import *
from .preprocess_files import *
from .lora_manager import *

def set_seed(seed: int = 42) -> None:
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # When running on the CuDNN backend, two further options must be set
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # Set a fixed value for the hash seed
    os.environ["PYTHONHASHSEED"] = str(seed)
    print(f"Random seed set as {seed}")

if os.getenv("RANDOM_SEED") is not None:
    set_seed(int(os.getenv("RANDOM_SEED")))
else:
    set_seed(42)
