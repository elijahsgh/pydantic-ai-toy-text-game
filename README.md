# Pydantic AI Toy Text Game
## Explanation
This is a very small example of using [Pydantic AI](https://ai.pydantic.dev/).

The agent plays the role of the game master of a very silly text based game where the player is a very clumsy adventurer.

## Concepts
### Configuration
Pydantic AI agents are configured through their Agent instance.

For Google related products, you can provide an API key to Gemini through the GEMINI_API_KEY env var or by loading the api_key, as this example does, through configuration. I have put the key in a .env file which you will need to provide.

```python
model = GeminiModel('gemini-1.5-flash', api_key=settings.gemini_api_key)
```

If the `api_key` parameter here is removed then Pydantic AI will look for a GEMINI_API_KEY env var.
You can generate API keys with [Google AI Studio](https://aistudio.google.com/) 

### Responses
The agent response we have defined contains a single parameter to tell us how much damage the player has taken (`damage_taken`) along with a text response.

### Variables
We use `player_hp` to track state between requests. This reperesents the player's health.

## Demo
```
$ uv run python main.py
I am a very clumsy adventurer sitting peacefully in a chair. How much health do I have?
You are sitting peacefully in a chair. You have 10 health remaining.
I stubbed my toe.
You stubbed your toe and take 1 damage. You have 9 health remaining.
I fell out of my chair.
You fell out of your chair and take 3 damage. You have 6 health remaining.
A bus struck me.
A bus struck you and you take 10 damage. You have 0 health remaining. Game Over.
```
