Keycloak Authentication with FastAPI
====================================

Keycloak provides a secure way to authenticate and authorize users in your application. In this project, we use the OpenID Connect protocol provided by Keycloak.

### Configuration

1. **Client Configuration in Keycloak**

   - Log in to the Keycloak admin console.
   - Create a new client for your FastAPI application.
   - Set the "Access Type" to "confidential" and configure the "Redirect URIs" for the FastAPI endpoints.
   
2. **Environment Variables**

   In your FastAPI project, you'll need to configure environment variables for Keycloak:

   .. code-block:: bash
   
      KEYCLOAK_SERVER_URL=https://keycloak.example.com/auth
      KEYCLOAK_REALM=myrealm
      KEYCLOAK_CLIENT_ID=myclient
      KEYCLOAK_CLIENT_SECRET=mysecret

3. **Middleware for Authentication**

   Use FastAPI's middleware to protect your routes:
   
   .. code-block:: python
   
      from fastapi import Depends, FastAPI
      from keycloak import KeycloakOpenID

      app = FastAPI()

      keycloak_openid = KeycloakOpenID(server_url="https://keycloak.example.com/auth/",
                                       client_id="myclient",
                                       realm_name="myrealm",
                                       client_secret_key="mysecret")

      def get_current_user(token: str = Depends(oauth2_scheme)):
          user_info = keycloak_openid.userinfo(token)
          return user_info
