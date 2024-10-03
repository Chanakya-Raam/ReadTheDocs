Authentication with Keycloak
============================

This section describes how to integrate FastAPI with Keycloak for user authentication and authorization.

Keycloak provides a REST API for:
- User login
- Token retrieval
- Session management

Endpoints:
----------

- **/auth/realms/{realm}/protocol/openid-connect/token**
  - *Description:* Retrieve access token.
  - *Method:* POST
  - *Request Body:*
    - `grant_type`: Type of request (e.g., password)
    - `client_id`: Client identifier
    - `client_secret`: Client secret
    - `username`: User’s username
    - `password`: User’s password
  - *Response:*
    ```json
    {
      "access_token": "eyJhbGciOiJSUzI1NiIsInR...",
      "refresh_token": "eyJhbGciOiJSUzI1NiIsInR...",
      "token_type": "bearer",
      "expires_in": 300
    }
    ```

- **/auth/admin/realms/{realm}/users**
  - *Description:* Create a new user in Keycloak.
  - *Method:* POST
  - *Request Body:*
    ```json
    {
      "username": "newuser",
      "enabled": true,
      "credentials": [
        {
          "type": "password",
          "value": "Password123",
          "temporary": false
        }
      ]
    }
    ```
  - *Response:*
    - `201 Created`: User created successfully
    - `409 Conflict`: Username already exists

