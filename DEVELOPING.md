# Project Structure

```bash
libica/
│
├── src/
│   ├── __init__.py                         # Root package initializer
│   ├── logging.py                          # Provides common logging configurations used across the application
│   │
│   ├── libica/                             # libica provides calls to IBM Consulting Assistants
│   │   ├── ica_audit.py                    # Provides audit functionalities for logging and tracking within ICA
│   │   ├── ica_base.py                     # Defines a private base class for ICA modules to share common attributes and methods
│   │   ├── ica_catalog.py                  # Manages the ICA catalog services, inherits from ICABase
│   │   ├── ica_client.py                   # Implements client interactions for ICA AI App management, extends ICABase
│   │   ├── ica_error.py                    # Custom error classes and exception handling specific to ICA
│   │   ├── ica_metering.py                 # Manages metering services for ICA, utilizing the ICABase framework
│   │   ├── ica_notification.py             # Handles notifications within ICA, using base functionalities from ICABase
│   │   ├── ica_settings.py                 # Contains settings specific to ICA (configurations and constants)
│   │   ├── __init__.py                     # Initializes the libica sub-package and sets up logging configurations
|   |   └── py.typed                        # Typing configuration for mypy
│   │
│   ├── icaclient/                          # icaclient provides commandline tools
│   │   ├── __init__.py                     # Sets up the icaclient sub-package and configures logging for client interactions
|   |   ├── py.typed                        # Typing configuration for mypy
│   │   ├── assistants.py                   # Commandline tool entrypoint, calls interactive_prompt for `icacli interactive`
│   │   └── interactive_prompt.py           # Supports interactive prompt features for command-line utilities
│   │
│   ├── consulting_assistants_ansible/      # provides ansible modules
│   │   └── consulting_assistants.py        # Manages consulting functionalities tailored for use with Ansible integrations
│   │
├── tests/                                  # Tests directory structured to reflect src/ hierarchy
│   ├── libica/                             # Tests for libica
│   │   ├── test_ica_audit.py               # Unit tests for ica_audit.py
│   │   ├── test_ica_base.py                # Unit tests for ica_base.py
│   │   ├── test_ica_catalog.py             # Unit tests for ica_catalog.py
│   │   ├── test_ica_client.py              # Unit tests for ica_client.py
│   │   ├── test_ica_error.py               # Unit tests for ica_error.py
│   │   ├── test_ica_metering.py            # Unit tests for ica_metering.py
│   │   ├── test_ica_notification.py        # Unit tests for ica_notification.py
│   │   └── test_ica_settings.py            # Unit tests for ica_settings.py
│   │
│   ├── icaclient/                          # Tests for icaclient
│   │   ├── test_interactive_prompt.py      # Test interactive prompt
│   │   └── test_assistants.py              # Unit tests for assistants.py
│   │
│   ├── consulting_assistants_ansible/      # Tests for ansible modules
│   │   └── test_consulting_assistants.py   # Unit tests for consulting_assistants.py
|   └── test_readme.py                      # Test examples in documentation with pytest-examples
│
├── Makefile                                # Provides commands for building, running, and testing the application
└── pyproject.toml                          # Configuration file for tooling and package management, using PDM
```


## Running a local travis build

```
https://github.com/travis-ci/travis.rb?tab=readme-ov-file#installation

sudo apt install ruby
gem install travis --user-install
```
