import asyncio

class AutoTyper:
    def __init__(self, bot, interval=0.5, default_message="Hello! This is an Automated Message. 🚀"):
        """
        Initializes the AutoTyper class to support multiple guilds.
        """
        self.bot = bot
        self.interval = interval
        self.default_message = default_message
        self.tasks = {}  # Dictionary to store tasks for each guild {guild_id: task}
        self.messages = {}  # Store custom messages for each guild {guild_id: message}
        self.interval = {} # Stores intervals per guild

    async def _sendMessages(self, guild_id, channel_id):
        """
        Sends messages periodically in a specific guild.
        """
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(channel_id)

        if not channel:
            print(f"Error: Could not find channel with ID {channel_id} in Guild {guild_id}")
            return

        while guild_id in self.tasks:  # Keeps running unless stopped
            try:
                message = self.messages.get(guild_id, self.default_message)
                await channel.send(message)
                print(f"Message sent successfully in Guild {guild_id}.")
            except Exception as e:
                print(f"Error sending message in Guild {guild_id}: {e}")

            await asyncio.sleep(self.interval)

    def start(self, guild_id, channel_id):
        """
        Starts the auto-typer for a specific guild.
        """
        if guild_id not in self.tasks:
            self.tasks[guild_id] = self.bot.loop.create_task(self._sendMessages(guild_id, channel_id))
            print(f"AutoTyper started in Guild {guild_id}.")

    def stop(self, guild_id):
        """
        Stops the auto-typer for a specific guild.
        """
        task = self.tasks.pop(guild_id, None)
        if task:
            task.cancel()
            print(f"AutoTyper stopped in Guild {guild_id}.")
        else:
            print(f"No AutoTyper running in Guild {guild_id}.")

    def setMessage(self, guild_id, new_message):
        """
        Updates the message for a specific guild.
        """
        self.messages[guild_id] = new_message
        print(f"AutoTyper message updated in Guild {guild_id}: {new_message}")

    def setInterval(self,guild_id,new_interval):
        """
        Changes the interval of the bot sending message periodically.
        Interval must be in seconds.
        :param new_interval:
        :param guild_id:
        :return:
        """
        if guild_id in self.tasks:
            self.interval[guild_id] = new_interval
            print(f"AutoTyper interval updated to {new_interval} seconds in Guild {guild_id}.")
        else:
            print(f"AutoTyper is not running in Guild {guild_id}.")













