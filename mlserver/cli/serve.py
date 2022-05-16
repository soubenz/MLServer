import os
import sys

from typing import List, Tuple, Union

from ..storage import get_models_storage
from ..model import MLModel
from ..repository import ModelRepository
from ..settings import Settings, ModelSettings
from cloudpathlib import CloudPath
from pathlib import Path
from google.cloud import storage
import os
DEFAULT_SETTINGS_FILENAME = "settings.json"


async def load_settings() -> Tuple[Settings, List[MLModel]]:
    """
    Load server and model settings.
    """
    # NOTE: Insert current directory and model folder into syspath to load
    # specified model.

    # t = await get_models_storage()


    # if folder:
    #     sys.path.insert(0, folder)

    # settings = None
    # # if _path_exists(folder, DEFAULT_SETTINGS_FILENAME):
    # #     settings_path = os.path.join(folder, DEFAULT_SETTINGS_FILENAME)  # type: ignore
    # #     settings = Settings.parse_file(settings_path)
    # # else:
    settings = Settings()

    # if folder is not None:
    settings.model_repository_root = '/tmp/models'

    models = []
    # if settings.load_models_at_startup:
    repository = ModelRepository('/tmp/models')
    available_models = await repository.list()
    
    models = [_init_model(model) for model in available_models]
    

    return settings, models


def _path_exists(folder: Union[str, None], file: str) -> bool:
    if folder is None:
        return False

    file_path = os.path.join(folder, file)
    return os.path.isfile(file_path)


def _init_model(model_settings: ModelSettings) -> MLModel:
    model_class = model_settings.implementation
    return model_class(model_settings)  # type: ignore
