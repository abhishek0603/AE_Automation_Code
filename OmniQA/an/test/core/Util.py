from datetime import datetime, timedelta
import time
import uuid


class TimeoutError(Exception):
    pass

DEFAULT_TIMEOUT = 30 # seconds FIXME move to config file


def wait_until(condition, timeout=DEFAULT_TIMEOUT, sleep=1, pass_exceptions=False, message=None):
    last_exception = None
    end_time = datetime.now() + timedelta(seconds=timeout)
    while datetime.now() < end_time:
        try:
            if condition():
                return True
        except Exception as e:
            if pass_exceptions:
                raise e
            else:
                last_exception = e
        time.sleep(sleep)

    if message:
        if last_exception:
            raise TimeoutError(message, e)
        else:
            raise TimeoutError(message)
    else:
        if last_exception:
            raise TimeoutError("Timed out.", e)
        else:
            raise TimeoutError("Timed out.")


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length]

def get_env(url):
    if 'dev' in url:
        folder_name = "dev"
    elif 'stg' in url:
        folder_name = "stg"
    elif 'qa' in url:
        folder_name = "qa"
    else:
        folder_name = "prod"

    return folder_name