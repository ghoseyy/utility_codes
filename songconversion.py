from pydub import AudioSegment
import os

def convert_to_mp3(input_file, output_file=None):
    if not os.path.exists(input_file):
        print("Error: Input file does not exist.")
        return

    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".mp3"

    try:
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="mp3")
        print(f"Conversion successful! Saved as {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "/path/"  # Replace with your file
    convert_to_mp3(input_file)
