# Running the Application with Docker Compose

Before running the project, you need to set up the required environment variables:

Copy the `.env.example` file to a new file named `.env`:

```bash
cp .env.example .env
```

To run the application using Docker Compose, execute the following command in your terminal:

```bash
docker-compose up -d
```

# Choice of Framework & Library

**Please explain why you chose the particular framework or library.**

- **Benefits & Drawbacks:**

  - I chose Django and Django Rest Framework with PostgreSQL for the database because Django abstracts a lot of the basic code and is "batteries included," which helps to create features faster. I have also used Redis cache for caching the get requests.

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

- When one queries the doctor, then clinic details are also shown, even though clinic data is in another table. Also, when I create a doctor, I am passing the clinic detail as well.

## API Usage

Here's an example of how to make a POST request to create a doctor:

```sh
curl  -X POST \
  'http://127.0.0.1:8000/api/doctor/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "clinic": {
    "name": "TH Medical Centre",
    "address": "Shop 2, G/F, Treasure Garden, 1 On Chee Road, Tai Po, New Territories",
    "district": "New Territories"
  },
  "consultation_detail": {
    "inclusive": true,
    "days": 3,
    "consultation_fee": "200.00",
    "member_exclusive_price": "150.00"
  },
  "schedule": [
    {
      "day_of_week": "Monday",
      "start_time": "09:00:00",
      "end_time": "20:00:00"
    },
    {
      "day_of_week": "Wednesday",
      "start_time": "09:00:00",
      "end_time": "13:30:00"
    },
    {
      "day_of_week": "Thursday",
      "start_time": "09:00:00",
      "end_time": "20:00:00"
    },
    {
      "day_of_week": "Saturday",
      "start_time": "15:00:00",
      "end_time": "20:00:00"
    }
  ],
  "phone": [
    "29730773",
    "29730833"
  ],
  "name": "Au Lik Hang",
  "speciality": "General Practitioner",
  "language": "English"
}'
```
Here's an example of how to make a GET request to get all doctors:

```sh
curl  -X GET \
  'http://127.0.0.1:8000/api/doctor/' \
  --header 'Accept: */*'
  ```

  Here's an example of how to make a GET request to get a doctor with id:

```sh
curl  -X GET \
  'http://127.0.0.1:8000/api/doctor/<id>' \
  --header 'Accept: */*'
  ```

Here's an example of how to make a GET request to get a doctor with some query params:

  ```sh
  curl  -X GET \
  'http://127.0.0.1:8000/api/doctor?language=English&district=New%20Territories&price_min=100&price_max=500&speciality=General%20Practitioner' \
  --header 'Accept: */*'
  ```