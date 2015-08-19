How to Make a Twitter Bot in Python
===================================

* Make a virtualenv
* Install [Tweepy](http://docs.tweepy.org/en/latest/getting_started.html): `pip install tweepy` or `pip install -r requirements.txt`
* Get your Twitter API keys and put them in the `settings.py.txt` file. Change the name of `settings.py.txt` to `settings.py`. It will not be added to version control.
* Open a Python terminal and type: `from bot import api`
* You can then use all of the methods on the `api` object. For example, type `user = api.get_user('CodeSelfStudy')` and then `print(user)` or `dir(user)` to see more about that user object.
