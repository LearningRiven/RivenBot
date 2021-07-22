# Discord bot developed by Yoda#3381

## File Structure
* main.py
* Cogs
  * channel.py
  * database.py
  * user.py
* DevTools
  * debugger.py
  * keep_alive.py
  * refresh_tools.py
* README.md

## Classes

  ### Main
  #### **main.py** - Main Runner for the bot
  #### **README.md**  - What you are reading now.... duh

  ### Cogs
  #### **channel.py** - All commands dealing with channels
  #### **user.py** - All commands dealing with users


  ### DevTools

  #### **keep_alive.py**    - WebServer for making sure the bot is always running on an address
  #### **debugger.py**      - Add methods in future for debugging
  #### **refresh_tools.py** - toolkit for refreshing the cogs in the app

## Idea

I always wanted to make my own discord bot, figured creating a server centered around a different idea (learning video editing) was the perfect opportunity

You can checkout any videos that I have on [youtube](https://www.youtube.com/channel/UCCGhjPI1FFlhmi-wvvB_EEw/featured)

## Releases
### Version 1.1 - Future Changes
* To Be Decided

### ~~Version 1.0 - Future Changes~~ - **RELEASED**

* Created the bot
* Added version control
* Added assigning a role to any user joining the server
* Added a WebServer to make sure the bot is always online
* Added structure for databasing if needed
* Added 'The Owner' specific commands
  * channel.py
    * .clear (amount) - default 5
      * Clears messages in a channel
  * refresh_tools.py
    * .load (fileName)
      * Loads a cog
    * .unload (fileName)
      * Unloads a cog
    * .refresh (fileName)
      * Refreshes a cog (unload then load it)
    * .refreshAll () - default 5
      * Refreshes the whole cog folder (unload then load it)

