# Test project to make django admin bug reproducible

I am using the latest django version (3.2.8) and I have the following problem:

1. My user can see model "inspection" via permisson "view_inspection"
2. My user cannot (!) see any foreign keys due to missing permissions
3. The readonly-foreign key is still rendered as a link which leads to a 403 page

What I need:

* Showing just the name of the object and not linking to it.

## Setup project

1. Install via pipenv (`pipenv install`)
2. Load fixtures (`python manage.py loaddata data`)
3. Log into admin with testuser|testTest12
4. http://127.0.0.1:8000/admin/testapp/myexamplemodel/1/change/
5. Click on linked foreign key "Test"
6. 403 page

