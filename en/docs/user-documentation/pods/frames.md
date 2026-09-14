# Create and use Frames

A Frame is an interactive file saved in a Pod. It can present a dashboard, report, or status view using Pod conversations, tasks, and files.

## Before you begin

Choose one purpose and the data it should show. Keep a pinned banner compact and glanceable. Decide whether the view is a generated snapshot or a configured view that reads saved Pod records and tasks.

## Create and pin a Frame

1. In a Pod conversation, ask an agent that can create Frames to build the view from named Pod sources.
2. Ask it to save the result in the Pod's **Files** area.
3. Open the Frame preview and check the layout, links, and displayed values.
4. From the file menu or preview, choose **Pin as Pod banner** if all members should see it at the top of Conversations.
5. Hover the banner to hide it for yourself, open it full screen, or unpin it if you are an Editor.

Only one Frame is pinned at a time. Pinning another Frame replaces the existing banner. Hiding the banner is personal; unpinning changes the Pod for everyone.

## Refresh a changing view

An ordinary generated Frame is a snapshot. To update it, ask an agent to read the latest Pod data and overwrite the same Frame, then review the new file. The banner remains attached to that file; it does not need to be pinned again after each overwrite.

A configured data-reading view can load saved Pod records and native Tasks when it opens and when you choose its **Refresh** action. It can update the display from those saved records without rewriting the Frame source each time. This is a read of the configured records while the view is open; it does not mean the view executes tasks in the background while closed.

When a value matters, keep the underlying task, file, or connected system as the source of truth. A checkbox or number shown in a Frame is a projection until the underlying record is saved and can be read back.

## What you should see afterward

Members see the pinned Frame when they open the Pod, and they can open the full file for detail. A snapshot shows its regenerated version; a configured data-reading view shows the latest saved records it can read after opening or refreshing.

## Common questions

### Why does the banner look different from the preview?

The banner and preview have different rendering space. Check the pinned view itself and simplify content that is clipped at the fixed height.

### Why is a value old after I changed a task?

For a snapshot, regenerate or overwrite the Frame. For a configured data-reading view, use **Refresh** and check that the underlying task was saved and is readable. Do not use a displayed value as proof that the source record changed.

### Who can pin or unpin a Frame?

Pod Editors manage the shared banner. Members can view it and can hide it for themselves.
