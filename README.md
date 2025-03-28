# easy-logger
Simple Wrapper of python Logger for easy usage

## Installation

### From cloned repo
```bash
git clone https://github.com/frmunozz/easy-logger.git
cd easy-logger
pip install .
```

### Directly with pip

```bash
pip install git+https://github.com/frmunozz/easy-logger.git
```

## Usage

### Direct Logger
```python
from elogger import create_logger

logger = create_logger(name="my_logger")
logger.info("This is an info message")
logger.error("This is an error message")
```

### Class integrated logger

```python
from elogger import LoggerMixin

class FOO(LoggerMixin):
    _log_file = "custom_log_file.log"

    def test_logger(self):
        self.logger.info("This is an info message")
        self.logger.error("This is an error message")

```

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your branch and create a pull request.

## License
This project is licensed under the MIT License.
