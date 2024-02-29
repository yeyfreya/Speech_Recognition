import os
import subprocess

# Specify the directory containing the .m4a files
source_directory = 'Suprised_wav'

# Loop through all files in the directory
for filename in os.listdir(source_directory):
    if filename.endswith('.m4a'):
        # Construct the full file path
        full_path = os.path.join(source_directory, filename)
        # Define the output file name (change extension to .wav)
        output_file = os.path.join(source_directory, os.path.splitext(filename)[0] + '.wav')
        
        # Construct the ffmpeg command
        command = ['ffmpeg', '-i', full_path, '-acodec', 'pcm_s16le', '-ar', '44100', output_file]
        
        # Execute the command
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Conversion completed.")
