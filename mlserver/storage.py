import os
import sys
from .settings import Settings, ModelSettings
from cloudpathlib import CloudPath, AnyPath


settings = Settings()

import os
DEFAULT_SETTINGS_FILENAME = "settings.json"

async def get_models_storage():
    print("getting models from storage")
    # sys.path.insert(0, ".")

    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="my_key.json"
    # bucket = client.get_bucket('users_artifacts')
    cloud_path = CloudPath(f"gs://users_artifacts/{settings.user}")
    local_path = AnyPath(f"/tmp/models")
    # print(list(root_dir.glob('**/**')))
    
    cloud_files_tmp = [p.parts[3:-1] for p in cloud_path.rglob('*/*/metadata.json')]
    local_files_tmp = [p.parts[3:-1] for p in local_path.rglob('*/*/metadata.json')]
    diff = list(set(cloud_files_tmp).difference(set(local_files_tmp)))

    # print(cloud_files_tmp)
    # print(local_files_tmp)
    # print(diff)
    # return
    cloud_path.copytree('/tmp/models/')
    print("finished copying models")
    return cloud_path.rglob('*/*/metadata.json')
