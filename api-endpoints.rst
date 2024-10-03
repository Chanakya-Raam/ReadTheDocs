API Endpoints
=============

This section lists available API endpoints for working with Keycloak.

Token Management
----------------

- **POST** `/auth/realms/{realm}/protocol/openid-connect/token`:
  - *Description:* Retrieve access token.

User Management
---------------

- **POST** `/auth/admin/realms/{realm}/users`:
  - *Description:* Create a new user in Keycloak.

- **GET** `/auth/admin/realms/{realm}/users`:
  - *Description:* Get a list of users in Keycloak.
