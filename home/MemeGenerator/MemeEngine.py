from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap


class MemeEngine:
    """Generates memes by adding quotes to images."""

    def __init__(self, output_dir: str):
        """Initialize MemeEngine with output directory.

        :param output_dir: directory to save generated memes
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """Create a meme with text and author.

        :param img_path: path to the image file
        :param text: quote text
        :param author: quote author
        :param width: maximum width of the image (default 500)
        :return: path to the generated meme
        """
        try:
            img = Image.open(img_path)

            # Resize image
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

            # Add text
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()

            # Wrap text
            text = f'"{text}" - {author}'
            wrapped_text = textwrap.wrap(text, width=40)

            # Random position for text
            x = random.randint(20, 50)
            y = random.randint(20, height - 100)

            # Draw each line of text
            for line in wrapped_text:
                draw.text((x, y), line, font=font, fill='white')
                y += 20

            # Save the meme
            out_path = os.path.join(self.output_dir, f"meme_{random.randint(0, 1000000)}.jpg")
            img.save(out_path)

            return out_path
        except Exception as e:
            print(f"Error generating meme: {e}")
            raise