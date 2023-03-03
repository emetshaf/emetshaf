![EMetshaf](https://github.com/emetshaf/media/raw/main/images/gh-banner.png?raw=true)

# 📗 Table of Contents

- [📖 EMetshaf ](#emetshaf)
  - [🛠 Built With](#built-with)
    - [🔭 Features](#features)
  - [🚀 Live Demo](#live-demo)
  - [💻 Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Usage](#usage)
  - [Screenshots](#screenshots)
  - [👥 Authors](#authors)
  - [🤝 Contributing](#contributing)
  - [❓ FAQ](#faq)
  - [📝 License ](#license)

# 📖 EMetshaf <a name="emetshaf"></a>

EMetshaf is an E-Book and Audio Book Store

## 🛠 Built With <a name="built-with"></a>

- API
  - Python / Flask
- WEB
  - Python / Flask

### 🔭 Features <a name="features"></a>

- [ ] Authentication
- [x] AudioBook Management
- [x] Author Management
- [x] Book Management
- [x] Category Management
- [x] Feedback management
- [x] Language Management
- [x] Narrator Management
- [x] Review Management
- [x] User Management

## 🚀 Live Demo <a name="live-demo"></a>

[Live Demo Link](https://mubareksd.tech)

## 💻 Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

- Python 3.9+

  - ubuntu/Debian

    ```sh
    sudo apt install python3
    ```

  - Arch/Manjaro

    ```sh
    sudo pacman -S python3
    ```

  - Redhat/Fedora

    ```sh
    sudo yum install python3
    ```

### Setup <a name="setup"></a>

- clones the project

  ```sh
  git clone https://github.com/emetshaf/emetshaf
  ```

- cd into the project

  ```sh
  cd emetshaf
  ```

- create virtual environment

  ```sh
  python3 -m venv env
  ```

- activate the environment

  ```sh
  source env/bin/activate
  ```

- install the required python packages

  ```sh
  pip install -r requirements.txt
  ```

### Usage <a name="usage"></a>

- start the api application

  ```sh
  tmux new-session -d 'gunicorn --config gunicorn-cfg.py run:api'
  ```

- start the web application

  ```sh
  tmux new-session -d 'gunicorn --config web/gunicorn-cfg.py run:web'
  ```

## Screenshots <a name="screenshots"></a>

| Page Name        | Index                                                 | Create                                                            | Edit                                                      |
| ---------------- | ----------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------- |
| Admin Dashboard  | ![admin_dashboard](./screenshots/admin_dashboard.png) |                                                                   |                                                           |
| Admin AudioBooks | ![admin_audiobooks](./)                               | ![admin_create_audiobook](./)                                     | ![admin_edit_audiobook](./)                               |
| Admin Authors    | ![admin_authors](./screenshots/admin_authors.png)     | ![admin_create_author](./screenshots/admin_create_author.png)     | ![admin_edit_author](./screenshots/admin_edit_author.png) |
| Admin Books      | ![admin_books](./screenshots/admin_books.png)         | ![admin_create_book](./)                                          | ![admin_edit_book](./)                                    |
| Admin Categories | ![admin_categories](./)                               | ![admin_create_category](./)                                      | ![admin_edit_category](./)                                |
| Admin Feedbacks  | ![admin_feedbacks](./)                                | ![admin_create_feedback](./)                                      | ![admin_edit_feedback](./)                                |
| Admin Languages  | ![admin_languages](./screenshots/admin_languages.png) | ![admin_create_language](./screenshots/admin_create_language.png) | ![admin_edit_language](./)                                |
| Admin Reviews    | ![admin_reviews](./)                                  | ![admin_create_review](./)                                        | ![admin_edit_review](./)                                  |
| Admin Users      | ![admin_users](./screenshots/admin_users.png)         | ![admin_create_user](./)                                          | ![admin_edit_user](./)                                    |

## 👥 Authors <a name="authors"></a>

👤 **Mubarek Seid Juhar**

- GitHub: [@mubareksd](https://github.com/mubareksd)
- Twitter: [@mubareksd](https://twitter.com/mubareksd)
- LinkedIn: [Mubarek Juhar](https://linkedin.com/in/mubareksd)

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

- Issues Bugs Feature Requests

  check out [issues page](../../issues/).

- Contributing

  check out [CONTRIBUTING.md](./CONTRIBUTING.md).

- Code of Conduct

  check out [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

## ❓ FAQ <a name="faq"></a>

## 📝 License <a name="license"></a>

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
