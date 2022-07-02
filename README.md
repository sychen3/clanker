# clanker

Usage: discord bot, reads chat and user activity and conducts bans based on chat activity and user status
      - any instance of 'token' or 'bannedWords' or 'bannedActivities' is imported from the botData.py file,
         not included in the github repository. Users may make their own.

Version History

0.5.1, 20220702: Code in the banned word tracker was made more efficient on flamelord1234's suggestions.
                Now converts the message content string to lowercase only once, rather than on each pass
                of the list.
                 Dittosalute and fronks2 responses added.
                 Standard updates to the blacklist.

0.5, 20220702:   Initial version (no github upload): disciplines user upon any instance of banned activity.
                Includes sending messages containing banned words or changing activity status to a banned
                activity.
                 on_member_update functionality added (checks user activity status whenever a user updates).
                 bot.run() commands disabled.
