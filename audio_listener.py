from pathlib import Path
from llama_index import download_loader
import configparser


def _get_configs(local_path, _vars):
    """
    extracts _vars value from local_path

    Parameters
    ----------
    local_path : string
        file variables path
    _vars : string
        variables to extract

    Returns
    -------
    tuple(str)* 
        a tuple with extracted variables.
    """
    config = configparser.ConfigParser()
    config.read(local_path)

    def get_config_from(section, variable_names):
        values = tuple(config.get(section, var) for var in variable_names)
        return values

    return get_config_from('variables', _vars)


audio_file_path, apikey = _get_configs("env_vars.ini", ["audio_path", "apikey"])

AudioTranscriber = download_loader("AudioTranscriber")

loader = AudioTranscriber()
documents = loader.load_data(file=Path(audio_file_path))
