import motor.motor_asyncio

from beanie import init_beanie


async def init_mongo_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("localhost", 27017)
    await init_beanie(database=client['logging'], document_models=['api.models.user_log.UserLog'])
