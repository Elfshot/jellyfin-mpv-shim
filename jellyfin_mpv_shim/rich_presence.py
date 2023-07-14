from pypresence import Client
import time

client_id = "990709917109354556"
RPC = Client(client_id)
RPC.start()


def register_join_event(syncplay_join_group: callable):
    RPC.register_event("activity_join", syncplay_join_group)


def send_presence(
    title: str,
    subtitle: str,
    library: str,
    playback_time: float = None,
    duration: float = None,
    playing: bool = False,
    syncplay_group: str = None,
):
    def media_text(media_type: str):
        match media_type:
            case "Anime":
                return {"large_t": "an Anime", "large_i": "anime"}
            case "Anime Movies":
                return {"large_t": "an Anime Movie", "large_i": "a_movie"}
            case "Kdrama":
                return {"large_t": "a Kdrama", "large_i": "kdrama"}
            case "Shows":
                return {"large_t": "a Show", "large_i": "show"}
            case "Movies":
                return {"large_t": "a Movie", "large_i": "movie"}
        return {"large_t": "Something", "large_i": "show"}

    media_group = media_text(library)
    small_image = "finger_heart"
    large_image = media_group["large_i"]
    large_text = "Watching " + media_group["large_t"]
    start = None
    end = None

    if playback_time is not None and duration is not None and playing:
        start = int(time.time() - playback_time)
        end = int(start + duration)

    RPC.set_activity(
        state=subtitle,
        details=title,
        instance=False,
        large_image=large_image,
        start=start,
        end=end,
        large_text=large_text,
        small_image=small_image,
        # party_id=str(hash(syncplay_group)),
        # party_size=[1, 100],
        # join=syncplay_group,
    )


def clear_presence():
    RPC.clear_activity()
