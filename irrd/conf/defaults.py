# In addition to these settings, simple
# defaults are stored in default_config.yaml.
from irrd import __version__

DEFAULT_SOURCE_NRTM_PORT = "43"
DEFAULT_SOURCE_IMPORT_TIMER = 300
DEFAULT_SOURCE_IMPORT_TIMER_NRTM4 = 60
DEFAULT_SOURCE_EXPORT_TIMER = 3600
HTTP_USER_AGENT = f"irrd/{__version__}"
