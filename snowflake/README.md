# API for Snowflake RBAC

Objective
Every domain admin need to grant access to their domain databases to whoever raised for access.

Try

1. We can have a end point with or without web UI to every domain admin.
2. Based on their domain, they have their own set of roles.
3. whenever they have the access request, they need to call the api with appropriate roles and date of access expiry.
4. we can maintain dash board to see the access management
5. WE can a script to revoke roles based on the date of access expiry.

