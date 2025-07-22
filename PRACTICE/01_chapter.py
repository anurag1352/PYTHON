#Question.1

print (''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

# Question.2
# Use REPL print 5 table

# Question.3
# Install external module and perform operation

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Durgesh Nai. 20 Rs daadi khakhori free")
engine.runAndWait()

# Question.4
import os

# Set the path to the directory (you can change this to any path)
directory_path = "C:/Users/dell/Desktop"

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print each item
print(f"Contents of directory: {directory_path}")
for item in contents:
    print(item)
