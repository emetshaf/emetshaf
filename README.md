#

![EMetshaf](https://github.com/emetshaf/media/raw/main/images/gh-banner.png?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
[![GitHub Issues](https://img.shields.io/github/issues/emetshaf/emetshaf)](https://github.com/emetshaf/emetshaf/issues)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://opensource.org/license/gpl-3-0/)

## Features

- [ ] Authentication
- [x] Author Management
- [ ] Book Management
- [ ] AudioBook Management
- [x] Category Management
- [x] Language Management
- [x] Review Management
- [x] User Management

## Setup

- clones the project

  `git clone https://github.com/emetshaf/emetshaf`

- cd into the project

  `cd emetshaf`

- create virtual environment

  `python3 venv env`

- activate the environment

  `source env/bin/activate`

- install the required python packages

  `pip install -r requirements.txt`

- start the api application

  `tmux 'gunicorn --config gunicorn-cfg.py api.v1.app:app'`

- start the web application

  `tmux 'gunicorn --config web/gunicorn-cfg.py web.app:app'`

### Docker

`docker compose up`

## Issues, Feature Requests and Contributing

<details><summary>Contributing</summary>

See [CONTRIBUTING.md](./CONTRIBUTING.md).

</details>

<details><summary>Code of Conduct</summary>

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

</details>

## FAQ

## License

    Copyright 2023 Mubarek Juhar

    Licensed under the GNU General Public License, Version 3.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    https://www.gnu.org/licenses/gpl-3.0.en.html

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
