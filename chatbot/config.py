#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os
from dotenv import load_dotenv


load_dotenv()  # to load our environment variables from the .env file.
class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    CLU_APP_ID = os.environ.get("CLUAppId", "")
    CLU_API_KEY = os.environ.get("CLUAPIKey", "")
    # CLU endpoint host name, ie "chatbot.cognitiveservices.azure.com"
    CLU_API_HOST_NAME = os.environ.get("CLUAPIHostName", "")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", ""
    )
