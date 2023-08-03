import asyncio

import label_studio_async_sdk as ls_sdk


TOKEN = '8b13e2070a8fa219d64d54277408d4ffae7fa768'


async def run():
    client = ls_sdk.Client(url='http://localhost:8080', api_key=TOKEN)
    project = await client.get_project(id=1)
    task_ids = await project.get_tasks_ids()
    tasks = await project.get_tasks()
    await project.delete_all_tasks()
    print(task_ids)
    print(tasks)
    await client.close()


if __name__ == '__main__':
    asyncio.run(run())
