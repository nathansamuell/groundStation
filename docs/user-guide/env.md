# The .env File

Many apps and software store data related to its current environment in a file called *.env*. Data can be stored in Key-Value pairs, like this:


```json
VARIABLE="value!"
```

Python can read these environment files using the following methods:

```python
load_dotenv()
os.getenv("<variable-name-here")
```

More information on these methods can be found [here!](https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/#)


## GroundStation's .env Variables
Below is a table of all currently configureable .env variables. Some variables are **required** for GroundStation to work properly. Sensible defaults are setup in the [install instructions](installation.md) Some variables are used only in development or testing. They are included here in case they are useful for your own setup troubleshooting. More information about developer variables can be found [here](../developer-reference/dev-landing.md)


|    Name                                | Required | Developer |
|  :--------:                            | :------: | :-------: |
| [USER_PASS](#env-variable-user_pass)   |     *    |           |
| MOCK_SERIAL                            |     *    |           |

### .env variable: USER_PASS