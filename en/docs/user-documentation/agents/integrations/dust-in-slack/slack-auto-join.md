# Automatically join new Slack channels

If Slack Auto-Join is enabled for the workspace, matching new public channels can be joined and synchronized automatically. This saves an administrator from adding each eligible channel manually. The feature applies to channels created after the pattern is configured; check existing channels separately.

## Configure a channel pattern

1. Confirm with a workspace administrator that Auto-Join is available and enabled.
2. In the Slack integration settings, enter a pattern that identifies only the public channels intended for synchronization.
3. Create a test channel whose name matches the pattern and verify that the integration joins it and begins syncing.
4. Check that the synchronized channel is added to the intended Space and that its audience is appropriate.

For example, a pattern such as `support-*` can match newly created channels such as `support-questions`. Keep patterns specific: a broad pattern can add unrelated conversations to the synchronized data set. Slack administrator permissions may be required to configure or change the integration.

Auto-Join does not make a private channel public or replace the need to review the destination Space's access. Verify what data is synced before relying on the new channel in Agent answers.
