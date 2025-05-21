# handsome_log

`handsome_log` is a universal logger designed for ETL pipelines, automation tasks, and web scraping scripts in Python.

This library is built on top of Python's standard `logging` module and the excellent `colorlog` package. Full credit and gratitude go to the developers of those foundational libraries.

The main goal of `handsome_log` is to provide custom log levels that make it easier to structure and monitor all stages of your data processes. These levels help you track your pipeline with meaningful, semantically distinct messages.

By default, the following custom levels are included:

| Level        | When to Use                                         | Color        |
|--------------|------------------------------------------------------|--------------|
| `STARTUP`    | When initializing or starting a process              | Bold Blue    |
| `VALIDATION` | When validating data, schema, or credentials         | Blue         |
| `DRY_RUN`    | For simulation runs that don't commit any changes    | Purple       |
| `SUCCESS`    | When a process completes successfully                | Bold Green   |
| `INFO`       | For general runtime information                      | Green        |
| `WARNING`    | When something unexpected happens, but the process continues | Yellow  |
| `ERROR`      | When a failure occurs but the system stays alive     | Red          |
| `CRITICAL`   | When a critical error occurs and the process halts   | Bold Red     |
| `DEBUG`      | For detailed technical/debugging messages            | Cyan         |

---

## Installation

Install via pip:

```bash
pip install handsome_log
```

## Features
Normal logging with colors

Normal logging without colors

For loop logging

## Usage 
To import and use the library you can use: 

```bash
#import
from handsome_log import get_logger 

#create logger object
logger = get_logger(__name__)

#testing different logging levels
logger.startup("Startup Script")
logger.info("General Info")
logger.validation("Validation Logging")
logger.dry_run("TEST RUN")
logger.success("Success information")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical Error")
```

![handsome_log_example_01](https://github.com/user-attachments/assets/dacbad77-5f89-410a-83bd-1e622f68e0ed)


