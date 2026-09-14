# Set up automatic replies in Slack channels

An Agent can be configured to respond in selected Slack channels without a member mentioning the workspace bot. This is useful for a dedicated question-and-answer channel, but can create noise in a general discussion channel. Confirm that the integration is enabled and the Agent is published before changing the channel settings.

## Choose where it replies

An administrator configures the behavior for each Agent in its **Slack Channel Settings**. Select the channel and enable **Respond to all messages in channel**. If the settings offer **Top-level posts only**, enable it to skip replies inside threads. Otherwise, the Agent may respond to both new channel posts and thread replies.

Messages that explicitly mention the bot continue to follow the mention behavior. Messages posted by other bots are ignored to avoid bot-to-bot reply loops.

## Private channels

A private channel must be available to the integration before it appears in the Agent's channel list. Depending on the setup, this can require adding the Slack tool to the Agent, connecting the appropriate Slack account, and inviting the integration to the channel.

## Check the result

Post a short test message in the selected channel, then test a thread reply if the mode allows it. Confirm that the intended Agent responded, that the audience can access its sources, and that unrelated channels remain unchanged. To change the behavior, return to the Agent's channel settings and save the updated selection.
