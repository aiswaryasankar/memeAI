import os, io
import base64
import weaviate
import random
import aiofiles

WEAVIATE_URL = os.getenv("WEAVIATE_URL")
CLIENT_CONFIG = None

if WEAVIATE_URL:
    access_token = os.getenv("ACCESS_TOKEN")
    if not access_token:
        raise ValueError(
            "ACCESS_TOKEN environment variable not set. "
            "This is needed to log into the Weaviate instance."
        )
    CLIENT_CONFIG = weaviate.AuthBearerToken(
        access_token=access_token, expires_in=300  # this is in seconds, by default 60s
    )
else:
    WEAVIATE_URL = "http://localhost:8080"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required for uploading objects to Weaviate")

CLIENT = weaviate.Client(
    WEAVIATE_URL,
    auth_client_secret=CLIENT_CONFIG,
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY},
)


def weaviate_text_search(text):
    """
    This function uses the nearText operator in Weaviate
    """
    source_text = {"concepts": text}

    weaviate_results = (
        CLIENT.query.get("Meme", ["description", "image"])
        .with_near_text(source_text)
        .with_limit(4)
        .do()
    )

    # WARNING: ONLY UNCOMMENT IF YOU ARE RUNNING INTO ISSUES GETTING QUERY RESULTS.
    # This WILL output the contents of two image files to your terminal window if you uncomment this.

    # print(f"Weaviate results: {weaviate_results}")
    # logger.info(weaviate_results)

    return weaviate_results["data"]["Get"]["Meme"]


async def return_meme(txt):
    query_results = weaviate_text_search(txt)
    if query_results is None:
        raise ValueError("No queries were returned. Please check your OPENAI_API_KEY.")
    file_names = []
    for i, res in enumerate(query_results):
        file_name = str(random.randint(0, 99999))
        description = res["description"]
        print(f"Description: {description}")
        decoded_img = base64.b64decode(res["image"])
        async with aiofiles.open(f"./assets/{file_name}.png", "wb") as f:
            await f.write(decoded_img)
        file_names.append(str(f"{file_name}.png"))
    return file_names
