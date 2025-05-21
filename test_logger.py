# Script to test all the options within handsome_log
from handsome_log import get_logger
import time


logger = get_logger("LOCAL_TEST", show_seconds=False)

logger.startup("Starting test pipeline")
logger.validation("Validating input")
logger.dry_run("Running dry simulation")
logger.success("Pipeline finished successfully")
logger.warning("Minor delay in response")
logger.error("Failed to write file")
logger.critical("System crash")
logger.debug("Debugging variable values")

for user in logger.loop_status(range(100), message="Extracting users", show_percent=True):
    time.sleep(0.02)
