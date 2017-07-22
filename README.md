# Scalable Bottle App

## Overview

Bottle's annotations are nice and dandy, but they can get in your way.

This web application demonstrates how you can work around that so your application becomes a bit less wildly and a bit more scalable in terms of code management and maintenance.

It may not look as pretty at first sight, but things become way easier this way.

To get it up and running, just call the `main.py` file:

```
python main.py
```

## Explanation

The key is to assign `bottle.default_app` to a variable (`app`) and then call the `get`/`post`/`route` methods on it (`app.get`/`app.post`/`app.route`) to map your routes to controller methods (here `web_app` acts as the controller). This means, you can now have multiple controllers mapped to various classes or dicts or lists or whatever you think fits your application's logical structure best.

This way, the sky becomes the limit. Now you can stick your route-controller mappings in a config file and read them on app start or stick them in various classes or split them across files or... Oh my!

Annotations can still be used, though. See `@bottle.error(404)`.

Also, pay attention to the `app.run` parameters which let you configure
your web app to your heart's content: host name, port number, automatic
reloading, debug mode. Again, you can stick those things in config files,
read them from environment variables, parse them from command line parameters etc.

Special Note: Here everything is crammed into a single file to allow a
quick overview, but the whole idea of this project structure is to give you the freedom to lay out your apps in the way that makes the most sense. Yes, a non-conventional project structuring may make it harder to maintain or extend a web application, but if you are smart about it, it may actually make it easier.
