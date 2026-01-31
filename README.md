## Security Design & Controls

This application was intentionally designed with security-first principles to
prevent common web application vulnerabilities.

### Authentication
- User passwords are hashed using Werkzeug’s secure hashing functions.
- Plaintext passwords are never stored or transmitted.

### Authorization
- JWT (JSON Web Tokens) are used for stateless authentication.
- Protected endpoints require a valid, signed JWT.
- Unauthorized requests are rejected with HTTP 401.

### Injection Prevention
- All database interactions use parameterized SQL queries.
- User input is never concatenated into SQL statements.
- This design prevents SQL injection attacks.

### Session Security
- Stateless JWT-based authentication eliminates server-side sessions.
- Reduces risk of session hijacking and fixation attacks.

### OWASP Top 10 Alignment
- Injection: Prevented via parameterized queries
- Broken Authentication: JWT + password hashing
- Sensitive Data Exposure: No plaintext credential storage
