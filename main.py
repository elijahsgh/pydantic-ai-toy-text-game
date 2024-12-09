from dataclasses import dataclass

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.gemini import GeminiModel

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    gemini_api_key: str


settings = Settings()

model = GeminiModel("gemini-1.5-flash", api_key=settings.gemini_api_key)


class AgentResult(BaseModel):
    response: str = Field(description="The response to the prompt provided.")
    damage_taken: int = Field(
        description="The damage received by the player.", ge=0, le=10
    )


agent = Agent(
    model,
    result_type=AgentResult,
    system_prompt="""
Based on the prompt decide a number between 1 and 10 that indicates how much damage the player has taken from the action described. Tell the player how much damage they haven taken. Finally, tell the player how much health they have remaining.
""",
)


@agent.system_prompt
def get_player_hp(ctx: RunContext[str]) -> str:
    return f"The player has {player_hp} health remaining."


if __name__ == '__main__':
    player_hp = 10

    injuries = ["I stubbed my toe.", "I fell out of my chair.", "A bus struck me."]

    prompt = "I am a very clumsy adventurer sitting peacefully in a chair. How much health do I have?"
    print(prompt)
    result = agent.run_sync(prompt, deps=player_hp)
    print(result.data.response)

    for injury in injuries:
        print(injury)
        result = agent.run_sync(injury, message_history=result.all_messages(), deps=player_hp)
        print(result.data.response)
        player_hp -= result.data.damage_taken
