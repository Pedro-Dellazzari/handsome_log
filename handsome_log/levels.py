import logging

# Custom log level values
SUCCESS_LEVEL = 25
STARTUP_LEVEL = 15
VALIDATION_LEVEL = 21
DRY_RUN_LEVEL = 16

# Register custom levels
logging.addLevelName(SUCCESS_LEVEL, "SUCCESS")
logging.addLevelName(STARTUP_LEVEL, "STARTUP")
logging.addLevelName(VALIDATION_LEVEL, "VALIDATION")
logging.addLevelName(DRY_RUN_LEVEL, "DRY_RUN")

# Custom log methods
def success(self, message, *args, **kwargs):
    if self.isEnabledFor(SUCCESS_LEVEL):
        self._log(SUCCESS_LEVEL, message, args, **kwargs)

def startup(self, message, *args, **kwargs):
    if self.isEnabledFor(STARTUP_LEVEL):
        self._log(STARTUP_LEVEL, message, args, **kwargs)

def validation(self, message, *args, **kwargs):
    if self.isEnabledFor(VALIDATION_LEVEL):
        self._log(VALIDATION_LEVEL, message, args, **kwargs)

def dry_run(self, message, *args, **kwargs):
    if self.isEnabledFor(DRY_RUN_LEVEL):
        self._log(DRY_RUN_LEVEL, message, args, **kwargs)

def register_custom_levels():
    """
    Binds custom logging methods to the Logger class.
    """
    logging.Logger.success = success
    logging.Logger.startup = startup
    logging.Logger.validation = validation
    logging.Logger.dry_run = dry_run
