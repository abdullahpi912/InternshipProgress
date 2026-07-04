# ============================================================
# app_config.py -- Task 2: App Config Lock (Tuple)
# ============================================================
APP_CONFIG = ("v1.0.3", "en", 30)  # (version, language, session_timeout_minutes)

version, language, timeout = APP_CONFIG  # unpack the tuple into named variables

print(f"App Version: {version}")
print(f"Language: {language}")
print(f"Session Timeout: {timeout} minutes")

# Tuples are locked once created -- the line below would crash the program:
# APP_CONFIG[1] = "fr"  # TypeError: 'tuple' object does not support item assignment
