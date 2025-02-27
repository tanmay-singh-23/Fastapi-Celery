import asyncio
import aiohttp

async def hit_endpoint(session, url, idx):
    try:
        async with session.get(url) as response:
            # Retrieve a snippet of the response text
            text = await response.text()
            print(f"Request {idx}: Status {response.status}, Response (first 100 chars): {text[:100]}")
    except Exception as e:
        print(f"Request {idx} failed: {e}")

async def run_requests(num_requests, url):
    async with aiohttp.ClientSession() as session:
        tasks = [hit_endpoint(session, url, i + 1) for i in range(num_requests)]
        await asyncio.gather(*tasks)

def main():
    try:
        num_requests = int(input("Enter the number of concurrent requests: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    endpoint_url = input("Enter the endpoint URL: ")

    asyncio.run(run_requests(num_requests, endpoint_url))

if __name__ == "__main__":
    main()
