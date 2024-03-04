# firebase-messaging
Small PoC using Firebase to send and receive messages

You need to create a Google Project with FireBase Cloud Messaging enabled and a linked Firebase Project with a web app

## Chrome Extension

Chrome Extension that register to firebase cloud messaging and prints received messages

You can build with

```sh
$ cd ChromeExtension
$ npm i
$ npm run build
```

then load the extension in Chrome from the `dist/` directory
Once started you can open the service worker console and you'll see a line like

```
FCM token <registration-token>
```

## Message Sender

Simple application to send a notification message to the extension

You can prepare the environment with 
```sh
$ poetry install
```

 And then run with 
 ```sh
 GOOGLE_APPLICATION_CREDENTIALS=<credentials-file-path> poetry run python ./message_sender/main.py <registration-token>
 ```

Once the message is sent you'll in the extension log something like
```sh
Message received: {..., notification: { body: "Hello again", title: "Hello" }, ...}
```

## Get App Config

Simple application to retrieve web app configuration to send to the extension

You can prepare the environment with 
```sh
$ poetry install
```

 And then run with 
 ```sh
 GOOGLE_APPLICATION_CREDENTIALS=<credentials-file-path> poetry run python ./get_app_config/main.py
 ```

The output should be something similar
```sh
Config: {'projectId': <project-id>, 'appId': <app-id>, ..., 'apiKey': <api-key>, ..., 'messagingSenderId': <sender-id>}
```
