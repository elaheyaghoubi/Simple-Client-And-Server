import asyncio
import websockets
import json
import time
from colorama import init, Fore, Style

init(autoreset=True)

async def async_number_sender(numbers):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:

        data = json.dumps(numbers)
        print(Fore.YELLOW + Style.BRIGHT + f"\n📦 Sending data: {data}")

        start = time.perf_counter()
        await websocket.send(data)
        print(Fore.GREEN + Style.BRIGHT + "✅ Data sent!\n")

        response = await websocket.recv()
        end = time.perf_counter()

        print(Fore.CYAN + Style.BRIGHT + f"📨 Server response: {response}")
        print(Fore.MAGENTA + Style.BRIGHT + f"⏱️  Round-trip latency: {(end - start)*1000:.2f} ms\n")


def number_collector():
    numbers = []

    print(Fore.MAGENTA + Style.BRIGHT + "\n✨ Number Collector ✨\n")
    print(Fore.CYAN + Style.BRIGHT + "Enter numbers (int or float). Type 'q' when done.\n")

    while True:
        value = input(Fore.BLUE + Style.BRIGHT + "> ").strip()

        if value.lower() == "q":
            break

        try:
            if '.' in value:
                num = float(value)
            else:
                num = int(value)

            numbers.append(num)
            print(Fore.GREEN + Style.BRIGHT + f"✔ Added {num}!\n")

        except ValueError:
            print(Fore.RED + Style.BRIGHT + "⚠️  Please enter a valid number (int or float) or 'q' to quit.\n")

    return numbers



if __name__ == "__main__":
    collected_numbers = number_collector()
    asyncio.run(async_number_sender(collected_numbers))