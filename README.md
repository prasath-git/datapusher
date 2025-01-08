# Datapusher

**Account Management**
**Base URL: /accounts/**
POST	/accounts/	                    Create a new account
GET	/accounts/<uuid:account_id>/	    Retrieve account details by account_id.
PUT	/accounts/<uuid:account_id>/	    Update account details by account_id.
DELETE	/accounts/<uuid:account_id>/	Delete an account. All associated destinations will be deleted.


**Destination Management
Base URL: /destinations/**
POST	/destinations/	             Create a new destination for an account.
GET	/destinations/<int:id>/	       Retrieve details of a destination by its id.
PUT	/destinations/<int:id>/	       Update details of a destination.
DELETE	/destinations/<int:id>/	   Delete a destination by its id.
