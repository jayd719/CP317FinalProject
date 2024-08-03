from typing import Any
from django.core.management.base import BaseCommand
from time import sleep
from os import path
from os import walk

class Command(BaseCommand):
    """
    -------------------------------------------------------
    Custom Django management command that writes messages to the console.
    It repeatedly writes "Hello World" to stdout and uses stderr to write a specified text.
    Use: python manage.py <command_name>
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        None
    -------------------------------------------------------
    """
    help= "BASE COMMAND"
    text_ = f'{__name__}'
    DUMMYFILES = [__name__,
                  '']
    
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        """
        -------------------------------------------------------
        Executes the main logic of the command. Writes a message to stderr, then
        repeatedly writes "Hello World" to stdout 10 times with a 0.5-second interval.
        Finally, calls a secondary function to write another message to stderr.
        Use: manage.py <command_name>
        -------------------------------------------------------
        Parameters:
            *args - Positional arguments passed to the command (Any).
            **options - Keyword arguments passed to the command (Any).
        Returns:
            str or None - The return type of the function (str | None).
        -------------------------------------------------------
        """
        self.getPath()
        self.stderr.write(self.text_)
        self.stdout.write(self.path)
        self.listFiles()
        
        
        
    
    def getPath(self):
        self.path = path.dirname(path.realpath(__file__)).replace("management/commands","")
        return self.path



    def listFiles(self):
        for (root, dirs, file) in walk(self.path):
            for f in file:
                if f.endswith(".py") or f.endswith(".js") or f.endswith('.html'):
                    print(path.join(root, f))
                    
    
    


            