Frequently Asked Questions (FAQ)
===============================

**Q: How do I refresh a user's access token?**

- To refresh the access token, use the `/auth/token/refresh` endpoint with the user's refresh token.

  Example request:
  
  .. code-block:: bash
  
     curl -X POST https://example.com/auth/token/refresh \
       -H "Content-Type: application/json" \
       -d '{"refresh_token": "eyJhbGciOiJSUzI1NiIsInR..."}'

**Q: How do I configure Keycloak to work in a production environment?**

- Ensure you use HTTPS for all communication between your FastAPI app and Keycloak.
- Set up high availability for your Keycloak instance using Keycloak's clustering capabilities.

**Q: Can I use Keycloak to handle authorization at the resource level?**

- Yes, Keycloak provides fine-grained resource-based authorization. You can configure this through the Keycloak admin console or via REST APIs.

