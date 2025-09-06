# FidoFido

It is a django-powered project now! \(Not a pure html+css+js project\)

## Initialization

### Dependencies

| \#   | dependencies | type         |
| ---- | ------------ | ------------ |
| 0    | git          | software     |
| 1    | python       | software     |
| 2    | django       | PyPI package |
| 3    | markdown     | PyPI package |

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
pip install -r requirements.txt # If you didn't installed Django and Markdown (These packages are REQUIRED!).
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # This command will ask you entering username, email and password.
python manage.py runserver
```
#### CMD & PowerShell
```powershell
# Step 1
git clone https://github.com/LiaoxyuCM/FidoFido.git
cd FidoFido
rd ./.git

# Step 2
pip install -r requirements.txt # If you didn't installed Django and Markdown (These packages are REQUIRED!).
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # This command will ask you entering username, email and password.
python manage.py runserver
```
