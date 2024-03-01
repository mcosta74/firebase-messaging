import sys

import firebase_admin
from firebase_admin import messaging


def main(args: list[str]):
    registration_token = args[0]

    firebase_admin.initialize_app()

    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title='Hello',
            body='Hello again',
        ),
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing registration token')
        sys.exit(1)

    main(sys.argv[1:])
