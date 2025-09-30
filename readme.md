# FidoFido

2 read English version of README.md please scroll down.

## 免责声明

FidoFido是一个尚未正式上线的论坛网站，命名可能与FIDO产生冲突。

FIDO是一个搞安全的标准。

所以，请勿将FidoFido与FIDO联系起来，作者不会承担FidoFido命名带来的后果。

## 警告

### 在fidofido/settings.py

1. 安全密钥是公开的。

## 预览

[点击跳转](https://fidofido-preview.rth1.xyz)

或者手动访问
https://fidofido-preview.rth1.xyz

### 备用网站

https://fidofido-preview.rth2.xyz

## 初始化

### 依赖列表

| \#   | 依赖名        | 类型         |
| ---- | ------------- | ------------ |
| 0    | git           | 软件         |
| 1    | python        | 软件         |
| 2    | django        | PyPI包       |
| 3    | markdown      | PyPI包       |
| 4    | whitenoise    | PyPI包       |
| 5    | python-dotenv | PyPI包       |

### 准备开始

如果你已经装了综上所述的依赖
（或者仅仅装了类型为软件的依赖）
请运行下面的命令开始。

#### Bash
```bash
# 第一步
git clone https://github.com/LiaoxyuCM/FidoFido.git
cd FidoFido
rm -rf ./.git

# 第二步
pip install -r requirements.txt # 如果你压根没装好综上所述的PyPI包（这些包都是必须的！）
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic # 如果不是第一次运行collectstatic的话，这个命令将会叫你"You have requested to collect static files at the destination location as specified in your settings file. This will overwrite existing files! Are you sure you want to do this?" （保留原文）输入"yes"继续。
python manage.py createsuperuser # 这个命令将会叫你输入用户名，邮箱（可留空）和密码。
python manage.py runserver
```

为了节省篇幅，如果你在cmd或者powershell运行此程序的话，把`rm -rf`改成`rd`即可。

### 添加.env文件

在项目目录"\\accounts\\"下新建一个名为`.env`的文件，内容如下：

```env
smtp_server=<你的SMTP服务器地址>
FidoFido_registeration_smtp_sender_email=<你的SMTP用户名>
FidoFido_registeration_smtp_password=<你的SMTP密码>
```

# FidoFido

## Disclaimer

FidoFido is a forum website that has not been officially published, and the naming may conflict with FIDO.

FIDO is a standard for security.

Therefore, please do not associate FidoFido with FIDO. The author will not bear the consequences of naming FidoFido.

## Warning

### In fidofido/settings.py

1. **SECRET_KEY is public.**

## Preview

[Click here](https://fidofido-preview.rth1.xyz/)

Or access manually:
https://fidofido-preview.rth1.xyz

### Alternative plan
https://fidofido-preview.rth2.xyz

## Initialization

### Dependencies

| \#   | dependencies | type         |
| ---- | ------------ | ------------ |
| 0    | git          | software     |
| 1    | python       | software     |
| 2    | django       | PyPI package |
| 3    | markdown     | PyPI package |
| 4    | whitenoise   | PyPI package |
| 5    | python-dotenv| PyPI package |

### Ready to Start

If you have already installed these dependencies
\(or only installed them that type is software\),
please run the following command to start.

#### Bash
```bash
# Step 1
git clone https://github.com/LiaoxyuCM/FidoFido.git
cd FidoFido
rm -rf ./.git

# Step 2
pip install -r requirements.txt # If you didn't installed the PyPI package listed above (These packages are REQUIRED!).
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic # If it's not your first time running this command, this command will ask you "You have requested to collect static files at the destination location as specified in your settings file. This will overwrite existing files! Are you sure you want to do this?" Enter "yes" to continue.
python manage.py createsuperuser # This command will ask you entering username, email(can be null) and password.
python manage.py runserver
```

To save space, if you are running this program in cmd or PowerShell, change `rm rf` 2 `rd`.

### Add .env file
In the project directory "\\accounts\\", create a new file named `.env`, with the following content:

```env
smtp_server=<your SMTP server address>
FidoFido_registeration_smtp_sender_email=<your SMTP username>
FidoFido_registeration_smtp_password=<your SMTP password>
```
