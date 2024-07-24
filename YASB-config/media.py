# media.py
import winsdk.windows.media.control
import asyncio
import json

async def get_media_info():
    session_manager = await winsdk.windows.media.control.GlobalSystemMediaTransportControlsSessionManager.request_async()
    current_session = session_manager.get_current_session()
    media_properties = await current_session.try_get_media_properties_async()
    media_playback_info = {
        "title": media_properties.title,
        "artist": media_properties.artist,
        "album": media_properties.album_title,
        "album_artist": media_properties.album_artist,
        "track": media_properties.track_number
    }
    print(json.dumps(media_playback_info))

async def pause_media():
    session_manager = await winsdk.windows.media.control.GlobalSystemMediaTransportControlsSessionManager.request_async()
    current_session = session_manager.get_current_session()
    await current_session.try_pause_async()

async def main():
    # Print media info
    await get_media_info()

    # Pause media playback
    await pause_media()

# Run the main function
asyncio.run(main())
