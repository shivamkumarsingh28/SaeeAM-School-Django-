./ngrok authtoken 1jskR6Sx3KzZTBwJAqqPe9Igaef_3o6wquwQBsztUrV59FRWA #For shiva850681@gmail.com email id 

# Django-School-Management-System

This app is meant to be used by school manager to manage their school records:
student data
staff
results and
finances.

It currently doesn't allow students/staff to login.
Solely, it's expected to be used on a single machine or online for managers only.

## Usage
It's best to install Python projects in a Virtual Enviroment. Once you have set up a VE, clone this project
```
Then

```bash
cd Django-School-Management-System
```
Run

```python
pip install -r requirements.txt #install required packages
python manange.py migrate # run first migration
python manange.py runserver # run the server
```
Then locate http://172.0.0.1:8000

## Admin Login
When you run migrate, a superuser is created.
```bash
username: admin
password: admin123
```

## Roadmap
To build a fully fledge open source school management for administrative use only.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Actively under development
