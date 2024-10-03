API Endpoints
=============

This section covers the available API endpoints in the FastAPI application, along with detailed descriptions, request formats, and sample responses.

Authentication Endpoints
------------------------

### **POST** `/auth/token`

- **Description:** Retrieve an access token from Keycloak.
- **Method:** `POST`
- **Headers:** 
  - `Content-Type: application/x-www-form-urlencoded`

- **Request Body Parameters:**
  - `grant_type`: The type of the OAuth2 flow (e.g., `password` for Resource Owner Password Credentials).
  - `client_id`: The ID of the Keycloak client.
  - `client_secret`: The secret key of the Keycloak client.
  - `username`: The username of the user requesting the token.
  - `password`: The password of the user requesting the token.

- **Sample Request:**

  .. code-block:: bash

     curl -X POST https://keycloak.example.com/auth/realms/{realm}/protocol/openid-connect/token \
       -d "grant_type=password" \
       -d "client_id=myclient" \
       -d "client_secret=mysecret" \
       -d "username=user1" \
       -d "password=pass1234"

- **Sample Response:**

  .. code-block:: json

     {
       "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI...",
       "expires_in": 300,
       "refresh_expires_in": 1800,
       "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
       "token_type": "Bearer",
       "not_before_policy": 0,
       "session_state": "abcd1234",
       "scope": "openid email profile"
     }


User Management Endpoints
-------------------------

### **POST** `/auth/admin/realms/{realm}/users`

- **Description:** Create a new user in the Keycloak realm.
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/json`

- **Request Body Parameters:**
  - `username`: The username for the new user.
  - `email`: The email address of the new user (optional).
  - `enabled`: Boolean to determine if the user is enabled.
  - `credentials`: List of credentials, such as passwords, for the new user.

- **Sample Request:**

  .. code-block:: json

     {
       "username": "newuser",
       "email": "newuser@example.com",
       "enabled": true,
       "credentials": [
         {
           "type": "password",
           "value": "Password123",
           "temporary": false
         }
       ]
     }

- **Sample Response:**
  - `201 Created`: User was successfully created.
  - `409 Conflict`: Username already exists.


### **GET** `/auth/admin/realms/{realm}/users`

- **Description:** Retrieve a list of all users in the Keycloak realm.
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <access_token>`

- **Query Parameters:**
  - `email`: Filter users by email (optional).
  - `username`: Filter users by username (optional).

- **Sample Request:**

  .. code-block:: bash

     curl -X GET https://keycloak.example.com/auth/admin/realms/{realm}/users \
       -H "Authorization: Bearer <access_token>"

- **Sample Response:**

  .. code-block:: json

     [
       {
         "id": "8f3f6a2b-e5e9-41ba-9eb2-7f98dfb8dbe8",
         "username": "user1",
         "email": "user1@example.com",
         "enabled": true,
         "firstName": "John",
         "lastName": "Doe"
       },
       {
         "id": "6c1f9a4a-e123-4b5b-9a2f-9c5f3af6d9e8",
         "username": "user2",
         "email": "user2@example.com",
         "enabled": true,
         "firstName": "Jane",
         "lastName": "Doe"
       }
     ]


Token Management Endpoints
--------------------------

### **POST** `/auth/realms/{realm}/protocol/openid-connect/token/introspect`

- **Description:** Check the validity of a token.
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/x-www-form-urlencoded`

- **Request Body Parameters:**
  - `token`: The access or refresh token to be introspected.
  - `client_id`: The client ID for authentication.
  - `client_secret`: The client secret for authentication.

- **Sample Request:**

  .. code-block:: bash

     curl -X POST https://keycloak.example.com/auth/realms/{realm}/protocol/openid-connect/token/introspect \
       -d "token=<access_token>" \
       -d "client_id=myclient" \
       -d "client_secret=mysecret"

- **Sample Response:**

  .. code-block:: json

     {
       "active": true,
       "scope": "openid email profile",
       "username": "user1",
       "exp": 1618878233,
       "sub": "abcd1234-5678-90ab-cdef-1234567890ab"
     }


### **POST** `/auth/realms/{realm}/protocol/openid-connect/logout`

- **Description:** Log the user out by invalidating the access token.
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/x-www-form-urlencoded`

- **Request Body Parameters:**
  - `client_id`: The client ID of the application.
  - `client_secret`: The secret key of the application.
  - `refresh_token`: The refresh token of the user to be logged out.

- **Sample Request:**

  .. code-block:: bash

     curl -X POST https://keycloak.example.com/auth/realms/{realm}/protocol/openid-connect/logout \
       -d "client_id=myclient" \
       -d "client_secret=mysecret" \
       -d "refresh_token=<refresh_token>"

- **Sample Response:**
  - `204 No Content`: Logout successful, tokens are invalidated.
  - `400 Bad Request`: Invalid request or token.


User Info Endpoints
-------------------

### **GET** `/auth/realms/{realm}/protocol/openid-connect/userinfo`

- **Description:** Retrieve information about the authenticated user.
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <access_token>`

- **Sample Request:**

  .. code-block:: bash

     curl -X GET https://keycloak.example.com/auth/realms/{realm}/protocol/openid-connect/userinfo \
       -H "Authorization: Bearer <access_token>"

- **Sample Response:**

  .. code-block:: json

     {
       "sub": "abcd1234-5678-90ab-cdef-1234567890ab",
       "name": "John Doe",
       "preferred_username": "user1",
       "email": "user1@example.com",
       "given_name": "John",
       "family_name": "Doe"
     }
