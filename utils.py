from PIL import Image
import base64
import io
import os

try:
    import openai
except ImportError:  # pragma: no cover - handled at runtime
    openai = None


def recognize_slide(image: Image.Image) -> str:
    """Analyze a slide image using EmatoGPT.

    The function expects the ``OPENAI_API_KEY`` environment variable to be set
    and sends the image to the EmatoGPT model hosted on the OpenAI platform.

    Args:
        image: PIL Image object representing the slide.

    Returns:
        str: Textual analysis provided by EmatoGPT or an error message.
    """

    if openai is None:
        return "openai package is not installed."

    if not os.getenv("OPENAI_API_KEY"):
        return "OPENAI_API_KEY is not configured."

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_b64 = base64.b64encode(buffered.getvalue()).decode()

    try:
        response = openai.ChatCompletion.create(
            model="emato-gpt",  # hypothetical GPT model for hematology
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are EmatoGPT, a model specialized in hematology slide"
                        " recognition."
                    ),
                },
                {
                    "role": "user",
                    "content": "Analyze this hematology slide image",
                },
            ],
            images=[{"type": "png", "data": image_b64}],
        )
        return response.choices[0].message.get("content", "No response")
    except Exception as exc:  # pragma: no cover - network failure
        return f"Error contacting EmatoGPT: {exc}"
