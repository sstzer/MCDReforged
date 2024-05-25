import dataclasses

from mcdreforged.constants import core_constant


@dataclasses.dataclass(frozen=True)
class MCDReforgedServerArgs:
	generate_default_only: bool = False  # If set to true, MCDR will only generate the default configuration and permission files
	initialize_environment: bool = False
	auto_init: bool = False
	config_file_path: str = core_constant.LOGGING_FILE
	permission_file_path: str = core_constant.PERMISSION_FILE_PATH
