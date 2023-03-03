| Issues                                                                                                                  | Pull Requests                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [![GitHub Issues](https://img.shields.io/github/issues/emetshaf/emetshaf)](https://github.com/emetshaf/emetshaf/issues) | [![GitHub Pull requests](https://img.shields.io/github/issues-pr/emetshaf/emetshaf)](https://github.com/emetshaf/emetshaf/issues-pr) |

# ![app icon](https://github.com/emetshaf/media/raw/main/images/app-icon.png) EMetshaf

EMetshaf is an E-Book and Audio Book Store

## Features

- [ ] Authentication
- [X] AudioBook Management
- [x] Author Management
- [X] Book Management
- [x] Category Management
- [X] Feedback management
- [x] Language Management
- [X] Narrator Management
- [x] Review Management
- [x] User Management

## Setup

- clones the project

  ```shell
  git clone https://github.com/emetshaf/emetshaf
  ```

- cd into the project

  ```shell
  cd emetshaf
  ```

- create virtual environment

  ```shell
  python3 venv env
  ```

- activate the environment

  ```shell
  source env/bin/activate
  ```

- install the required python packages

  ```shell
  pip install -r requirements.txt
  ```

- start the api application

  ```shell
  tmux new-session -d 'gunicorn --config gunicorn-cfg.py run:api'
  ```

- start the web application

  ```shell
  tmux new-session -d 'gunicorn --config web/gunicorn-cfg.py run:web'
  ```

### Docker

```shell
docker compose up
```

## Screenshots

| Page Name       | Screenshot |
| --------------- | ---------- |
| Admin Dashboard | ![admin_dashboard](./screenshots/admin_dashboard.png)           |
| Admin Authors | ![admin_authors](./screenshots/admin_authors.png) |
| Admin Create Author | ![admin_create_author](./screenshots/admin_create_author.png) |
| Admin Books | ![admin_books](./screenshots/admin_books.png) |
| Admin Languages | ![admin_languages](./screenshots/admin_languages.png) |
| Admin Create Language | ![admin_create_language](./screenshots/admin_create_language.png) |
| Admin Users | ![admin_users](./screenshots/admin_users.png) |

## Issues, Feature Requests and Contributing

<details><summary>Issues</summary>

</details>

<details><summary>Bugs</summary>

</details>

<details><summary>Feature Requests</summary>

</details>

<details><summary>Contributing</summary>

See [CONTRIBUTING.md](./CONTRIBUTING.md).

</details>

<details><summary>Code of Conduct</summary>

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

</details>

## FAQ

## License

```text
    Copyright 2023 EMetshaf

    Licensed under the GNU General Public License, Version 3.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    https://www.gnu.org/licenses/gpl-3.0.en.html

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
```
