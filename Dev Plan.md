# Development Plan

## Phase 0 — Foundation

### v0.1: Set up base system
- Initialize GitHub repo, define .env structure
- Create Flask app structure
- Define MySQL schema, ensure persistent storage
- Set up Docker container with bind mounts ([container name]/data)

### v0.2: Admin dashboard for system settings
- Flask Blueprint for admin panel
- UI for managing system-wide configurations
- Secure authentication (username/password)

### v0.5: Core Downloading engine
- yt-dlp wrapper for downloads
- Structured download queue & status updates
- Directory structure management

### v0.9: Channel Subscriptions
- Subscription logic (auto-download new content)
- User-level preferences for handling subscriptions

## Phase 1 — Core Functionality

### v1.0: Usable MVP
- Playback integration with Video.js
- Basic UI for browsing/downloading media
- API endpoints for adding URLs to queue

### v1.5: Basic Help
- Static help page covering key features
- Quick intro guide for non-tech users

## Phase 2 — UX Enhancements

### v2.0: Personalized Homepages
- User settings for home page layout
- Section customization & sorting options

### v2.2: iOS Shortcut + Bookmarklet
- Create iOS shortcut to send URLs to queue
- Develop bookmarklet for browsers

### v2.3: Browser Extensions
- Chrome/Firefox extension for pushing URLs to GruveTube

## Phase 3 — Usability Enhancements

### v3.0: Basic Toolbar
- Quick action buttons for common tasks

### v3.1: Enhanced Help (tooltips)
- Inline help for each major feature

### v3.2: Advanced Toolbar
- Customizable UI buttons
- Status panel for active downloads

### v3.5: Push Notifications
- Notify users when downloads complete

## Phase 4 — Advanced UI Customization

### v4.0: Styling/Theming
- Dark mode, custom themes

## Phase 5 — Advanced Content Management

### v5.0: Jellyfin Integration
- Ensure media files auto-sync properly

## Phase 6 — Extensibility and Power Features

### v6.0: Plugin architecture
- API structure for future integrations
