# GruveTube

A self-hosted, multi-user, personal/private YouTube with a clean, modern, customizable interface.

## Planned Features
- Multiple Options for downloading videos:
  - direct/start-now option for downloading a single video, audio-only portion of a video, or playlist
  - Download from a queue (a list of URLs in a text file - ytdl.list) with multiple options for adding videos/playlists to the queue:
    - browser extensions
    - bookmarklets
    - iOS Share Sheet shortcut
    - Subscribe to a channel to automatically download new videos as they are released. Optionally download existing channel videos:
      - all
      - limited
        - by number of videos
        - by age of video
    - As above but audio only (Music files). Optionally:
      - Exclude live performances
      - Include _only_ live performaces
- Customizable Home screen
  - Toolbar (user configurable) with Quick Access to Downloads, Help, Search library, much more
  - Section Visibility:
    - New Downloads
    - Playlists (sortable/filterable)
    - Pin specific playlists to top of Playlists section
    - Continue Watching
    - Watch History
    - Download History (completed downloads)
    - Full Library with sort/filter options
  - Section order
  - Layout (rows/columns) per visible section
- Jellyfin integration
- Extendable via plugins to support [yt-dlp](https://github.com/yt-dlp)'s huge [list of supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Tech Stack
Docker, Flask, MySql, yt-dlp, Video.js
