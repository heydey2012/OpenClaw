# OpenClaw Mobile Development Plan (v1.0)
**Date:** 2026-02-26
**Author:** PM Team (Kong)
**Status:** Initial Draft

## 1. Project Overview
- **Project Name:** OpenClaw Mobile (Codename: "Portable Claw")
- **Goal:** Launch a powerful, privacy-focused AI agent app for Android and iOS.
- **Vision:** "Your AI Agent, Everywhere." Transform the smartphone into an intelligent assistant that acts, not just chats.

## 2. Core Features (MVP)
The Minimum Viable Product (MVP) will focus on essential agent capabilities.

### A. Interface
- **Unified Chat UI:** Clean, messaging-style interface (Text & Voice).
- **Voice Mode:** Real-time voice interaction (STT/TTS) for hands-free use.
- **Widget Support:** Quick access from home screen/lock screen.

### B. Agent Capabilities (The "Claw")
Unlike standard chatbots, OpenClaw Mobile will have *agency*:
- **SMS/Message Integration:** Read and draft messages (Android: direct SMS access; iOS: via Shortcuts/Share Sheet).
- **Calendar & Reminders:** Full read/write access to system calendars.
- **Location Services:** Context-aware assistance (e.g., "Remind me when I get home").
- **Web Browsing:** Built-in browser for research and summaries.

### C. Architecture
- **Hybrid Model:**
  - **Cloud Relay:** Connects to a user's personal OpenClaw server (PC/Server) for heavy tasks (optional but recommended for power users).
  - **On-Device (Lite):** Basic chat and local tool execution using lightweight models (e.g., Gemini Nano or optimized small models) for offline capability.

## 3. Platform Specifics

### 🤖 Android (Team Droid)
- **Deep Integration:** Utilizing Android's flexible permissions for background services.
- **Automation:** Direct control over SMS, Calls, and Notifications.
- **Overlay:** "Chat Bubble" support for multitasking.

### 🍎 iOS (Team Apple)
- **Shortcuts Integration:** leveraging Siri Shortcuts to bypass sandbox limitations.
- **Share Sheet:** "Send to OpenClaw" for analyzing web pages/files from other apps.
- **Live Activities:** Real-time status updates on Lock Screen/Dynamic Island.

## 4. Development Roadmap

### Phase 1: Foundation (Weeks 1-4)
- [ ] Set up project repositories (React Native or Flutter for cross-platform core, or separate Native). **Decision needed.**
- [ ] UI/UX Design (Pixel Team).
- [ ] Basic Chat Interface implementation.

### Phase 2: Core Tools (Weeks 5-8)
- [ ] Calendar & Reminder integration.
- [ ] Location services.
- [ ] Basic Web Search.

### Phase 3: Advanced Features (Weeks 9-12)
- [ ] Voice Mode (STT/TTS).
- [ ] Android Background Services.
- [ ] iOS Shortcuts integration.

### Phase 4: Beta & Launch
- [ ] Internal Testing (Dogfooding).
- [ ] Store Submission (Google Play & App Store).

## 5. Next Steps
1.  **Tech Stack Decision:** Native (Kotlin/Swift) vs. Cross-Platform (Flutter/React Native). PM recommends **Flutter** for speed or **Native** for performance/access.
2.  **Server Strategy:** Will the app rely on a hosted OpenClaw instance (User's PC) or a cloud backend?

---
*Signed,*
*Kong (PM Team)*
