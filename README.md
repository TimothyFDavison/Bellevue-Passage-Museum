# Bellevue-Passage-Museum

Exploring the creation of digital avatars and other forms of immersive interaction with historical data.

### Step One - Create an LLM Digital Avatar
- Ingest MP3 file of BPM interview
  - Run diarization and transcription, extracting timestamps (using Scraibe)
- [TTS] Automatically segment the audio to create a subset which captures a given speaker
  - Train an RVC model on the speaker (using Applio)
  - Produce text in the voice of that speaker (using Applio)
- [LLM] Segment the interview into Q&A pairs
  - Create a Q&A agent to ask questions about the speaker's life
  - Use questions from the interview as a starting point, potentially retrieved from a database
- [ASR] Create a simple GUI to capture voice input and transcribe a user's dialogue
- **[ASR + LLM + TTS]** Combine workflows to allow real-time dialogue with the system
  - Optionally create a workflow to dialogue with the avatar directly
- [Visual Avatar - Image] Create an embedding to represent a person based on a set of uploaded images
- 