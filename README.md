# Work at Olist

This project is an webAPI used to record calls and return bill for an especific number.

To run this project you need to have an enviroment with django and djangorestframework

```
pip install django
pip install djangorestframework
python manage.py runserver
```

#### Examples body for post method for the end point

1. Call Start Record

```
http://localhost:8000/calls/
{
  "id":  // Record unique identificator;
  "type":  // Indicate if it's a call "start" or "end" record;
  "timestamp":  // The timestamp of when the event occured;
  "call_id":  // Unique for each call record pair;
  "source":  // The subscriber phone number that originated the call;
  "destination":  // The phone number receiving the call.
}
```

2. Call End Record

```
http://localhost:8000/calls/
{
   "id":  // Record unique identificator;
   "type":  // Indicate if it's a call "start" or "end" record;
   "timestamp":  // The timestamp of when the event occured;
   "call_id":  // Unique for each call record pair.
}
```

To get an bill for an especifc number you use a GET with number and date(not required)

### Example url to get number bills

1. Without a date(it will get the last month bill)
```
http://localhost:8000/calls/47996623579/
```
2. Passing a date
```
http://localhost:8000/calls/47996623579/2018-04-10/
```
