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

- [x] Authentication
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
- MariaDB
- Git
- Tmux

  - ubuntu/Debian

    ```sh
    sudo apt install python3
    sudo apt install mariadb-server
    sudo apt install git
    sudo apt install tmux
    ```

  - Arch/Manjaro

    ```sh
    sudo pacman -S python3
    sudo pacman -S mariadb
    sudo pacman -S git
    sudo pacman -S tmux
    ```

  - Redhat/Fedora

    ```sh
    sudo yum install python3
    sudo yum install mariadb-server
    sudo yum install git
    sudo yum install tmux
    ```

  - MacOS

    ```sh
    brew install python3
    brew install mariadb
    brew install git
    brew install tmux
    ```

  - Windows

    ```sh
    choco install python3
    choco install mariadb
    choco install git
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

- create a database

  ```sh
  mysql -u root -p
  ```

  ```sql
  CREATE DATABASE db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
  ```

- create a user

  ```sql
  CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'db_user_pwd';
  ```

- grant db_user all privileges on db_name

  ```sql
  GRANT ALL PRIVILEGES ON db_name.* TO 'db_user'@'localhost';
  ```

- flush privileges

  ```sql
  FLUSH PRIVILEGES;
  ```

- create a .env file

  ```sh
  touch .env
  ```

  ```sh
  touch .env
  ```

- add the following to the .env file

  ```sh
  SECRET_KEY=your_secret_key
  EMETSHAF_ENV=dev
  EMETSHAF_MYSQL_HOST=localhost
  EMETSHAF_MYSQL_USER=db_user
  EMETSHAF_MYSQL_PWD=db_user_pwd
  EMETSHAF_MYSQL_DB=db_name
  ```

### Usage <a name="usage"></a>

- start the api application
  - Linux/MacOS

    ```sh
    tmux new-session -d 'gunicorn --config gunicorn-cfg.py run:api'
    ```

- start the web application
  - Linux/MacOS

    ```sh
    tmux new-session -d 'gunicorn --config web/gunicorn-cfg.py run:web'
    ```

## 👥 Authors <a name="authors"></a>

👤 **Mubarek Seid Juhar**

- GitHub: [@mubareksd](https://github.com/mubareksd)
- GitLab: [@mubareksd](https://gitlab.com/mubareksd)
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
