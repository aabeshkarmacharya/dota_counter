# Dota 2 Utilities Discord bot

## To create a Discord Bot
- Go to https://discord.com/developers/applications
- Create a Discord account
- Create an application
    - Select new application
    - Input a name and click *Create*
- Navigate to the *Bot* tab on the left-hand navigation list
- Create a bot user, by selecting *Add Bot* and confirming. You'll see the new bot user in the portal.
 (Notice that, by default, your bot user will inherit the name of your application)
- (*Optional) Change the name of the bot
- Create a Discord server
    - Go to [your Discordhome page](https://discordapp.com/channels/@me) or app
    - Select the + icon on the left-hand side of the page to add a server
    - This will present two options, Create a server and Join a Server. 
    In this case, select Create a server and enter a name for your server
- Register the bot with your server
    - Go to [Developer Portal](http://discordapp.com/developers/applications)
    - Select the OAuth2 page from the left-hand navigation
    - Scroll down and select bot from the SCOPES options and check required BOT PERMISSIONS. 
    Discord will generate your application’s authorization URL with the selected scope and permissions
    - Select Copy beside the URL that was generated for you and paste it into your browser
    - Select your server from the dropdown options and click *Authorize*
- Done

### Installation
Install the requirements:
```shell script
pip install -r requirements.txt
```
Go to the Bot page in [Developer Portal](https://discord.com/developers/applications) 
and click copy under the token section.

Create a `.env` file like below and paste the token:
```shell script
DISCORD_TOKEN=1234567890abcdefghijklmnopqrstuvwxyz
````
