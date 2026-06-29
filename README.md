# ACN Auth_keys.json Setups
*None of the files in here will work in the FreeSoul ACN server, only custom servers you manually add these Auth_keys.json files to.

Auth Keys in All City Network handle badges, admin status, and special modes like pvp. However, if you know nothing about code, it can be confusing to figure out how to work them exactly, which is what this repo is here for. You can browse one of the pre made auth_keys files, or use the infomation below to make your own

## Auth_key.json Explained:
The auth_key.json is a file where you make special keys for badges, admins, and players with special effects. For each key you make, you just make a new entire set of "userkind, badges, tags, key, and description". It must be formated correctly though.

- **The Pre-made auth_keys.json files can be found here ->** https://github.com/SnailUsbs/ACN-Auth_keys.json-Setups/tree/main/Premade%20Auth_keys.json%20files

- **If you just want to automate the entire auth_key.json proccess, you can use:** https://github.com/SnailUsbs/ACN-Auth_keys.json-Setups/blob/main/auth_keys_manager.py


- **Where Do The Players Put The Auth Key?:** Players add their key in the config/BombrushMP/auth.txt file. You can search "auth" in the R2ModMan config editor as well to easily find it.

## User Kinds:
The user kind option in the auth_keys.json file is how you can gives yourself or others Admin/Mod perms. 

<details>
  <summary><b>Player</b></summary>
  
  - **Player** By default, all players are set to "Player", which doesn't grant the user any special features.
</details>

<details>
  <summary><b>Mod</b></summary>
  
  - **Mod** Setting the userkind to "Mod" grants that player various tools to help manage the players in the server, alongisde a badge to show other players they are a mod. These include commands to:

  - handle banning users (/banaddress , /banid , /unban , /banlist )

  - get player information (/getids , /getaddresses)

  - clear chat for all players (/clearall)

  - see server stats (/stats)

  - spy on players (/lurk)

  - server tag management (/getservertags , /removeservertag , /setservertag)

- various special skin commands (/makeseankingston , /makesteve , /makeminecraft , /makeredxmas). 
</details>

<details>
  <summary><b>Admin</b></summary>
  
  - **Admin:** Setting the userkind to "Admin" gives that user everything "Mod" does, but with server management added on top. These server management features include:

  - reload the auth keys and banned users (/reload)

  - restart the entire server (/restart)

  - send a message to a given stage or the entire server as a whole (/say , /sayall).
</details>

## Badges:
Badges are a special image that appear beside the username of players. You can either set badges through specific auth keys, or give them to all players.

- **Badge ID:** The badge ID is what you actually put in the badge section of the auth_key.json. In the following link you can find all badges, with them being named their ID: https://github.com/LazyDuchess/BombRushMP/tree/main/Thunderstore/plugins/badgemap

- **How To Give Everyone The Same Badge:** You can give all players in your server badges through the default auth key, which will be the only auth key option in the json file by default. Anything put in here will not require your users to input a special auth key, so everything in there gets applied to all players.

- **Special Mod Badge:** granting a player with the userkind "Mod" gives them badge "0" , which is the star. 

## Tags:
Tags are an option in auth_keys that allow you to give players special effects. Below are all of the possible tags you can use, and what they do:

- **elite:** Gives the player a special skin, a special skateboard skin, allows them to use /lurk without being a mod, and gives them a special leave/join message.
- **pvp:** enables pvp
- **canthit:** makes it to where the user can not be hit from pvp
- **nodamage:** makes the player immune to damage
