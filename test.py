import asyncio
from redis.asyncio.cluster import RedisCluster  # type: ignore
import redis.asyncio as redis  # type: ignore

async def main():
    r = RedisCluster.from_url("redis://localhost:16379/0")
    p = r.pipeline()
    p.json().set("blah", ".", 1)
    p.set("blah2", 1)
    await p.execute()


    p = r.json().pipeline()
    p.set("blah3", ".", 1)
    await p.execute()
    print("done")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(main())