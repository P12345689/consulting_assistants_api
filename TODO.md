# PRIORITY

- [ ] Add platform / OS / Python to version information
- [ ] validate emailAddress and team name.. check that it exists for all get_security_key. Validate team name exists.
- [ ] Put the test X or PASS in front of the heading
- [ ] Strip the title, etc. fields when retrieving info on assistants etc. as a table, and also make them all one-line (strip newlines)
- [ ] Expand tags etc. that are as json, flatten, remove the name for example in tags.
- [ ] Build: FileNotFoundError: [Errno 2] No such file or directory: 'aspell'
- [ ] Make some of the ICAClient methods private.
- [ ] Raise this instead: {'error': 'Exactly one of model_id_or_name, assistant_id, or collection_id must be provided.'}
- [ ] Check if JSON response from the API has any content, is there, for example, any model listed in the getModels?
- [ ] # TODO: implement a 15 minute caching of the chat_id, reusing it create_chat_id - configurable, can be turned off, will retry if no cache / expired
- [X] get_transaction_response should return a STR
- [ ] Makefile build to update svg files with updated scores before publishing
- [ ] Add warnings not just log.debug, log to file

# TODO for interactiv_prompt.py

- [ ] src/icacli/interactive_prompt.py:225:29: W0511: TODO: load this into the 'editor', like a user would type in the text.. use prompt_toolkit (fixme)
- [ ] src/icacli/interactive_prompt.py:248:78: W0511: TODO: make this loop back to entering a tag (fixme)
- [ ] TODO: the API returns a space in front of the response string for some reason. To report as bug, then I can remove the strip() in print(response["response"].strip())
- [ ] Use https://python-prompt-toolkit.readthedocs.io/en/master/
- [ ] Move RENDER_MARKDOWN_OUTPUT = False to settings
- [ ] Fix refresh_data
- [ ] Fix when it exits when an invalid option is provided
- [ ] /assistant breaks when it gets an invalid tag `TypeError: cannot unpack non-iterable NoneType object`
- [ ] ^C should stop a current prompt, but NOT exit interactive mode.
- [ ] Use safe_print when using rich print, should be a common library

# TODO

- [ ] Rename as consulting_assistants_api due to libica name conflict on pypi
- [ ] /add file.txt, need to make it edit the prompt dynamically (interactive)
- [ ] Common logging format for all in __init__, separate logging.py, log method name, etc/
- [ ] Fix collections so that it's consistent and ALSO returns a LIST like all the other APIs instead of collections['collections'] being a list.
- [ ]  Check that model id exists.. see test_get_model_id_by_name
- [ ]  Fix transactionId string - consitent API returns + log the actual received json
- [ ] Centralize logging to file
- [ ] Assistants, models, etc. are NOT printed in the id order, add a sort.
- [X] validator is deprecated in Pydantic, migrate to v2
- [X] Function to keep trying to get the response every configurable seconds, for a maximum number of seconds when using async.
- [ ] Pick what to install install libica[langchain] or libica[cli]
- [X] Configurable support for the config file and cache file location. Should also attempt to create the directory. Maybe try different locations ~/.config, /tmp, etc. via mktmp. Add config clear flag.
- [ ] Add a clear cache option to remove all cache. Make dir configurable.
- [ ] Cache requests by model as well! As long as the parameters and all data are the same.
- [ ] Cache chat_id for 15 min.
- [ ] Add support to initialize with a different key: client = ICAClient(assistants_api_key=os.env(MYINTEGRATION_ASSISTANTS_API_KEY))
- [ ] Check that the config exists and don't error out if it doesn't... I can't run setup-config atm if the sample is not in place!
- [ ] Add a model=? parameter that can be an id, a document collection or a name..
- [ ] Can use names instead of id for assistants?
- [X] Add a retry mechanism / flag / config (ex: ASSISTANTS_RETRY_ATTEMPTS=2)
- [ ] Stats support, like tokens/second, time per request, other info etc outputting to stderr + log file
- [X] Add --system-prompt-file to prompt
- [ ] Make the test compare to the comment next to each command, something like # {errorcode=0, grep="string to grep for"}

# Fix me

- [ ] Set a COMMAND='PYTHONPATH=$(pwd)/src:$PYTHONPATH coverage run --append --source=$(pwd)/src ./src/icacli/assistants.py' or icacli
- [ ] Check that only one input is supported icacli prompt --assistant-id=7825 --prompt "What is OpenShift" --model_id_or_name=123 # for example, this should error out
- [ ] The response still prints a space at the start.
- [ ] Parameters don't seem to work at the moment, ex: `icacli prompt --prompt "What is k8s" --parameters='{"temperature": 1, "min_new_tokens": "100", "max_new_tokens": 100}'` does not return 100 tokens.
- [ ] 100% test coverage, will need smocker for it to mock API for failed responses
- [ ] Unify execute with execute_async and prompt options?
- [ ] Add substitutionParameters test cases
- [ ] JSON output support for each of the calls. output=json or output=text for the libica calls with a configurable default?
- [ ] Instantiate the config in the class.
- [ ] icacli prompt --prompt --system-prompt-file test/system-prompt.txt --prompt "" # Test system prompt file Empty prompt fails?

# Bugs to report in API Docs or API

- [ ] x-security-key incorrectly spelled x-securitykey in the documentation
- [ ] parameters don't work
- [ ] systemprompt does not work
- [ ] There is a bug in the swagger where this returns RAW not JSON using the APi Client (getSecurityKey) - this breaks the swagger send command



## Other issues

```
src/libica/ica_model.py:658:5: PYD002 Non-annotated attribute inside Pydantic model
src/libica/ica_model.py:942:5: PYD001 Positional argument for Field default argument
src/libica/ica_model.py:987:5: PYD001 Positional argument for Field default argument
src/libica/ica_settings.py:165:5: PYD002 Non-annotated attribute inside Pydantic model
```
