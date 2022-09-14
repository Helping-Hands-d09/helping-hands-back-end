# Helping hands back end

## Test Coverage

- 1-use `coverage run manage.py test`
- 2-run `coverage html`
- 3-hit this route `http://127.0.0.1:5500/htmlcov/index.html`

## Deployed back-end

Link: [https://helping-hands-api.herokuapp.com](https://helping-hands-api.herokuapp.com)

Endpoints:

**Main**:

- admin/
- accounts/
- api/v1/users/
- api/v1/campaign/
- api/v1/connection/
- api/v1/user-post/
- api/token/
- api/token/refresh/
- api-auth/

**Other for formatting and registering**:

- api/v1/users/register
- api/v1/campaign/location
- api/v1/campaign/location/[id numbser]
- api/v1/campaign/category
- api/v1/campaign/category/[id number]
- api/v1/connection/campaign-members/[campaign id number]
- api/v1/connection/member-campaigns/[member id number]
- api/v1/user-post/postcomment/[post id to get all it's comments]
