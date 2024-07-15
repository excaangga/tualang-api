# AI Dungeon Master (DM) Server

This Flask-based server acts as an AI Dungeon Master (DM) to guide users through their role-playing game (RPG) adventures. I use huggingchat API to access the LLM. As for the DM, it provides information about characters, settings, and encounters. Here's how it works:

## Getting Started

1. **Installation**:
   - Clone this repository to your local machine.
   - Set up cookies and your env containing secrets from HuggingFace (you can look up the steps on HuggingChat API repository)

2. **Environment Variables**:
   - Set the following environment variables:
     - `EMAIL`: Your email address (used for authentication).
     - `PASSWD`: Your password (used for authentication).

3. **Run the Server**:
   - Execute `python3 server.py` to start the Flask server.
   - The server will run at `http://localhost:5000/`.

## Endpoints

1. **Root Endpoint** (`/`):
   - Returns a simple message indicating that the server is working.

2. **Initiate Endpoint** (`/initiate`):
   - Provides an introduction for the AI Dungeon Master (DM).
   - Instructs users to ask for their character's name, race, class, and level.
   - Once provided, the DM starts creating the character's backstory and campaign.

3. **List Conversations Endpoint** (`/list`):
   - Lists available conversations (campaigns) with their unique IDs.
   - Users can choose a conversation to interact with.

4. **Chat Endpoint** (`/chat/<chat_id>`):
   - Handles user messages within a specific conversation.
   - Supports both POST (for sending messages) and DELETE (to end a conversation).

## Usage

1. Start the server.
2. Initiate a conversation by accessing `/initiate`.
3. Choose a conversation from the list using `/list`.
4. Interact with the AI Dungeon Master by sending messages to `/chat/<chat_id>`. This endpoint supports both POST and DELETE method.
