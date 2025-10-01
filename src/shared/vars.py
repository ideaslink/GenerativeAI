"""
parameters and environment vars

__author__ = "vci"
__copyright__ = "Copyright 2025, vci
__license++ = "MIT
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "contact@hsharp.com"
__status__ = "development"
__reference__ = "vci"

"""


"""
Google Cloud Platform (GCP) environment variables
These variables are used to configure the GCP client

You need to set these variables in your environment, e.g. 

    setx API_KEY "YOUR_API_KEY"

The above setup is to avoid revealing sensitive information in your codebase.
"""

GCP_VARS = {
    "API_KEY": "API_KEY",
    "API_KEY_VERTEX" : "API_KEY_VERTEX"     
}


"""
OpenRouter environment variables
These variables are used to configure the OpenRouter client

You need to set these variables in your environment, e.g. 

    setx OR_API_KEY "YOUR_OpenRouter_API_KEY"

The above setup is to avoid revealing sensitive information in your codebase.
"""

OPENROUTER_VARS = {
    "API_KEY": "OR_API_KEY"     
}