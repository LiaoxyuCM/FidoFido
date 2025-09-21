# FidoFido

It is a django-powered project now! \(Not a pure html+css+js project\)

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
python manage.py collectstatic # This command will ask you "You have requested to collect static files at the destination location as specified in your settings file. This will overwrite existing files! Are you sure you want to do this?" Enter "yes" to continue.
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
pip install -r requirements.txt # If you didn't installed the PyPI package listed above (These packages are REQUIRED!).
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic # This command will ask you "You have requested to collect static files at the destination location as specified in your settings file. This will overwrite existing files! Are you sure you want to do this?" Enter "yes" to continue.
python manage.py createsuperuser # This command will ask you entering username, email and password.
python manage.py runserver
```

## Short stories

### How does Fido come from?

This word "Fido" comes from
**Old version of PEP-English Textbook / Grade 5-Volume II / Unit 5 "Whose dog is it?" / Section B / Let's talk.**

![Fido's origin](https://github.com/user-attachments/assets/d893fb05-5735-4a29-b097-b3625c1acfbe)

Fido is a dog.

