# python-scripts

Collection of useful and interesting Python scripts

## Howto run python scripts in virtual environment

1. Install virtual environment
   ````
   install python3.11-venv
   ````
2. Create virtual environment
   ````
   python -m venv <virtual_env_name>
   ````
3. Activate virtual environment
   ````
   source <path_to_virtual_venv_name>/bin/activate
   ````  
5. Run script in virtual environment
   ````
   python audio_book.py
   ````
6. Deactivate a virtual environment
   ````
   deactivate
   ````

## List of Scripts

1. audio_book.py: convert text_file to mp3 file (requirements: `gTTS` --> `pip install gTTS`)
2. console_calendar.py: create and print a calendar after entering the year
3. figlet_message_color.py: output a text used figlet font (requirements: `termcolor`, `pyfiglet` --> `pip install termcolor pyfiglet`)
