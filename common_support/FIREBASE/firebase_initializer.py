import firebase_admin
import requests
from firebase_admin import credentials

# initialize firebase if not initialized

creds = {"type": "service_account",
         "project_id": "lazafron-cloud",
         "private_key_id": "8f6426919049bff88140994aaf998ce7890f8a6c",
         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC7bx8sb0izF"
                        "+V3\nhSzx23GwQ7sBeTPX9r+U5e0lpPQp+aOSJUmVdDoMEouS8/XZBLVWVADKjQ/JJoCL\noUh5QJW1b"
                        "/60tTNBJa1Vjg7G4Ltj+0JUYuAy9KRjA2+pLeQ+CVX2KZJsKRa9GL28"
                        "\nvdBiDmb7UG9M2xYcMoQvn2jaE7NpSoO8oJiVPcKUpNNhpYumLn+1DJicYfmJhjWU\n"
                        "+LTindklH3eb1D0YJrY1n3vY2nswNBzmUQcQOwxhZunfOa5ovDXBwTfh0yQjhJRS\nPjf"
                        "+JS12uoK2FMcgy2yZYpffrLHJ8sHh0Y3YJ5gAELre7wZ6G41lqwBFFZD6E8Qo\nxIWZwy7jAgMBAAECggEAArCXDW"
                        "+xZuSOZfcyzGu+R23JZr2DCXPgjvX3v8UMvfd3\nqfbABhWLabXwa9T1b75aDdmZw05f7h6P1LElVZwgKeDoElbRW"
                        "/t679Hgk2kRN1+Z\nNZXPqtuI6mTXuuFON7exlJ1HHSc/zMnomydMMMQNJUkjt8IjIJd2/yn1+r8yoW2q"
                        "\niMkkOVsMaNVyLPkWw28EeDZzs04sR9jHDYrPJmLH/nMy8exenJt8Hut/pkXbQqPe\ngjR3rTlXpx7qRvl"
                        "/tt6GW9Cn4ZFnUCeJYzFlZq82g3d1lpeyBl9NLIv+RYjrHLz0\nbAO6FgoA1zsWka5+qA5+aTW"
                        "+/cxwSrGJJPdDbE1jGQKBgQDi/AGUmj7limnLqsjq\nUwSXCif19MAn0q2nvtzHVsktuDkY+cSCrsBUcz"
                        "+2Ml3QYnv1m12aRYIQJ7Zh6PzZ\nOg9A8rAR7hCIsQxi4j0ZkhIM4n5fZYr2sAPWs9MkZGG4j1hgw2siUWLXRndDpNfD"
                        "\nEzGkYuT9/9Yh9P/xiEkhgHdVuQKBgQDTZNfm2zXpL0ncuryVNLzI5ORjBu9fHU/N"
                        "\nlEZ5ZtSzzO6zQKp2O6UPlQViXHK5GEQFhTUObImoIH4z4if1Vlnf5LPeKvA7e34r"
                        "\nhdbETbGgmSROTrEdUUCQW6XSD9wmXuxERjx5eNy9H2uE5jy7+H9au7AK1R9KPMnU\nZU327jR3ewKBgQCw"
                        "/i7BUHFhDcgnPxoB1hBLMmksmdfIdbhhiCuh6KNg2jjzp7c6"
                        "\n68cfUurISIfsuQ7N2oNni3G65SyLNmELhgFk9Jikso0D+YKeDKn2KXeXwnkmLAjr\nCR9FKN2oj/m/L0"
                        "+LzHXawbmgAdt3zK9N9saL122WPgscWW3GSi40SHdFSQKBgQCf\nViV"
                        "+dsCd8OzlmUNH26Zobk7PbYzDzp42QIsWOrIcjF1nc1iJIc/6fMLALxqx9V5g"
                        "\nItWo95qSxVsa1F52CA5aOlJxJUBKNX0WZR1KfZ1jhcrd02agyHu307ybJyUzLt07\nYQ14KeeIDcTHOZuRu26S"
                        "/2Fj6Nxa4pLmqy0m8MlPPQKBgQDd5EtCxl7gwyEFslxY\nD1RCmv18in06eJwh/3ZL5psO3HS/8wEacd2sC2Wb9gT"
                        "/Pau8suYU6LLW5yMGEKos\nEXA28ibv9yK8rEcUnZtSoK8SxhH1A+b6rKz8kqDDZJI7XOgmky8jUfi3SL80wHzc"
                        "\nGfNgw+IjbA1CtkU+m3JBtjoe7w==\n-----END PRIVATE KEY-----\n",
         "client_email": "firebase-adminsdk-mw3pc@lazafron-cloud.iam.gserviceaccount.com",
         "client_id": "110323579871385072386",
         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
         "token_uri": "https://oauth2.googleapis.com/token",
         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-mw3pc"
                                 "%40lazafron-cloud.iam.gserviceaccount.com "
         }


def initialize_app():
    try:
        # noinspection PyProtectedMember
        if not firebase_admin._apps:
            firebase_admin.initialize_app(credentials.Certificate(creds),
                                          {'storageBucket': 'lazafron-cloud.appspot.com',
                                           'databaseURL': 'https://lazafron-cloud-default-rtdb.firebaseio.com/'
                                           })
            print("Firebase initialized")
            return True
        else:
            print("Firebase already initialized")
            return False
    except Exception as e:
        print("Error initializing firebase")
        print(e)
        return False


def have_internet():
    try:
        requests.get('http://google.com', timeout=5)
        return True
    except:
        return False
