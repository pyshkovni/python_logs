# -*- coding: utf-8 -*-

log_config = {
    "version": 1,
    "formatters": {
        "handlers_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "main_formatter": {
            "format": "%(asctime)s - %(message)s"
        },
    },
    "handlers": {
        "handlers_handler": {
            "class": "logging.FileHandler",
            "formatter": "handlers_formatter",
            "filename": "handlers.log",
            "encoding": "UTF-8",
        },
        "main_handler": {
            "class": "logging.FileHandler",
            "formatter": "main_formatter",
            "filename": "main.log",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "handlers": {
            "handlers": ["handlers_handler"],
            "level": "DEBUG",
        },
        "main": {
            "handlers": ["main_handler"],
            "level": "INFO",
        },
    },
}

