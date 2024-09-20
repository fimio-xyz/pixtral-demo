import asyncio
from PIL import Image
from service import VLLM  # Import the VLLM class from service.py

async def main():
    # Instantiate the VLLM class
    vllm_service = VLLM()

    # Load an example image (you need to have an image named 'example_image.png' in your project directory)
    image = Image.open("example_image.png")

    # Call the generate method with default parameters
    print("Generating output with default parameters...")

    # Initialize an empty list to store the generated text parts
    output_parts = []

    # Concatenate the output from the async generator
    async for output in vllm_service.generate(image):
        output_parts.append(output.strip())  # Strip leading/trailing whitespaces for each part

    # Join all parts into a single string and fix spacing issues
    full_output = ' '.join(output_parts).replace(" .", ".").replace(" ,", ",")

    # Print the final properly parsed output
    print(full_output)

# Entry point to run the async function
if __name__ == "__main__":
    asyncio.run(main())
