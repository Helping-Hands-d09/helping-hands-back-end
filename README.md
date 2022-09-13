# Helping hands back end

## Test Coverage

- 1-use `coverage run manage.py test`
- 2-run `coverage html`
- 3-hit this route `http://127.0.0.1:5500/htmlcov/index.html`

## Deployed back-end

Link: [https://helping-hands-api.herokuapp.com](https://helping-hands-api.herokuapp.com)

Endpoints:

- admin/
- ^swagger(?P<format>\.json|\.yaml)$ [name='schema-json']
- ^swagger/$ [name='schema-swagger-ui']
- ^redoc/$ [name='schema-redoc']
- accounts/
- api/v1/users/
- api/v1/campaign/
- api/v1/connection/
- api/v1/user-post/
- api/token/ [name='token_obtain_pair']
- api/token/refresh/ [name='token_refresh']
- api-auth/

**Note: There is more but I need to go, will continue tomorrow...**
