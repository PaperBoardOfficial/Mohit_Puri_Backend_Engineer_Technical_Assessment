# Running the Application with Docker Compose

To run the application using Docker Compose, execute the following command in your terminal:

```bash
docker-compose up -d

# Choice of Framework & Library

**Please explain why you chose the particular framework or library.**

- **Benefits & Drawbacks:**
  - I chose Django and Django Rest Framework with PostgreSQL for the database because Django abstracts a lot of the basic code and is "batteries included," which helps to create features faster.

- **Assumptions Underlying the Choice:**
  - I assumed speed is not a big issue. I have used WSGI for Django. I could have used FastAPI if speed was a concern.

# Potential Improvement

**Please elaborate on what kind of improvements you would like to implement if given more time.**

- I could have implemented internationalization (support for multiple languages) and the bulk create aspect mentioned in the bonus part if I had more time.

# Production Consideration

**Any extra steps should be taken with caution when deploying your app to a production environment?**

There are several steps which can be taken:

1. Use environment variables or Django's `django-environ` package to manage sensitive information securely.
2. Set `DEBUG` to `False`.
3. Set `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` to `True`.
4. Use Django's `SecurityMiddleware` and the `SECURE_SSL_REDIRECT` setting to redirect all non-HTTPS traffic to HTTPS.
5. Ensure `X_FRAME_OPTIONS` is set to `DENY` or `SAMEORIGIN` to protect against clickjacking.
6. Run `python manage.py check --deploy` to check for deployment readiness.

# Assumptions

**Any assumptions you have made when you designed the data model and API schema?**

- Yes, I assumed that a clinic can have multiple doctors. A doctor can have multiple phone numbers.

**Any other assumptions and opinions you have taken throughout the assessments?**

- I assumed that it is a simple project; hence, I did not use Redis cache. Also, when one gets the doctor, then clinic details are also shown, even though clinic data is in another table. Also, when I create a doctor, I am passing the clinic detail as well. Ideally, the frontend should first fetch different clinics from the backend and send the respective clinic id only to the backend while creating a doctor. This would ensure separation of concern. For this, I have created a List API for clinics.