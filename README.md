
## Thinkgs to know before testing
**Database Credentials:** in the ```settings.py``` file, assign you database credentials to the *DATABASE_USER* & *DATABASE_PASSWORD* variables.<br>
**HOST Variable:** make sure the HOST variable is correctly pointing to the DB server. ```localhost``` should be the default.


## API paths to test
```restaurant/``` - test loading of static files like the logo and template files<br>
```restaurant/menu/``` - get menu list OR post a new menu item (no authentication required)<br>
```restaurant/menu/1``` - get menu item<br>
```auth/users/``` - register a user<br>
```auth/token/login/``` - obtain auth token<br>
**OR**<br>
```api-token-auth/``` - obtain auth token *(API client like Insomnia only)*<br>
<br>
*Tip: How to use token in API client like Insomnia*

 1. Click the "Auth" dropdown list & select "Bearer"
 2. In the "Token" field, enter your token
 3. In the "Prefix" field, type "Token"

<img src="https://github.com/user-attachments/assets/7a2d8aad-e0f8-465f-a8fd-cebeddb6d092" width="50%" height="50%"><br><br>
```auth/token/logout/``` - to logout<br>
```restaurant/booking/tables/``` - make GET/POST requests to get & create bookings
