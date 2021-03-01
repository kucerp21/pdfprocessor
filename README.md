# PDF rendering service
This projects purpose is to accept .pdf files and normalize them. The whole service is 
available through API.

* [Setup and testing](docs/setup.md)

## Suggested ext steps
1. setup user authentication system (e.g. with tokens)
2. finish implementing pdfdocument testing
3. implement migration linter for migration testing
4. setup black (or other) for unanimous code formatting
5. setup NGINX
6. (prepare staging environment)
7. prepare production settings
8. setup secure location for production envs (e.g. vault)
9. create CI pipeline running all tests, migration linter, black etc
10. extend document app admin for better CC access