# Localizr
[wip] Locale files generator. because I hate updating locale files manually. It's prone to error because not all developers understand all those words. So give the Translator an access to a page where they can input those translations and developers will just do their job by fetching it automatically.


#### DEMO

You can access the demo pages with this credential:
```
username: demo
password: localizr
```

###### Admin page
http://app-localizr.herokuapp.com/admin

###### Strings Generator

http://app-localizr.herokuapp.com/app/demo-en


#### AUTO-DEPLOY TO HEROKU

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/michaelhenry/localizr)


## Format

#### iOS

```txt
"key" = "value";
```

#### Android

```xml
<resources>
  <string name="key">value</string>
</resources>
```

## Author

Michael Henry Pantaleon, me@iamkel.net

## License

Localizr is available under the MIT license. See the LICENSE file for more info.
