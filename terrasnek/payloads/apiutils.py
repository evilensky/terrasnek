import json
from json import JSONDecoder, JSONEncoder


def convert_key(key):
    """
    Converts a key from snake_case to lisp-case.
    """
    return "-".join([s.lower() for s in key.split("_")])


class LispCaseJSONEncoder(JSONEncoder):
    """
    Converts all keys from snake_case to lisp-case.
    """

    def default(self, obj):
        if isinstance(obj, dict):
            return {
                    convert_key(k): self.default(v)
                    for k, v in obj.items()
            }
        elif isinstance(obj, list):
            return [self.default(v) for v in obj]
        else:
            return obj


def dict_to_snake(d):
    return {
            convert_key(k): v
            for k, v in d.items()
    }


class LispCaseJSONDecoder(JSONDecoder):
    """
    Converts all keys from lisp-case to snake_case.
    """

    def __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, object_hook=dict_to_snake, *args, **kwargs)
