# streamlit_test
A test using Streamlit + FastAPI

This will try to use an MSAL connection, and then will run a llama_index instance to run some queries locally.

The following variables are required

export msal_client_id=CLIENT_ID
export msal_authority=https://login.microsoftonline.com/{YOUR_MSAL_AUTHORITY}

The following variables are optional and are used for logging purpuses

export instrumentation_key=INSTRUMENTATION_KEY